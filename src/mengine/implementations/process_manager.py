import logging

from src.mengine.exceptions.exceptions import ValidationError, HTTPException
from src.mengine.implementations.concrete_connection import ConcreteConnection
from src.mengine.interfaces.i_connection import IConnection
from src.mengine.interfaces.i_process_manager import IProcessManager
from src.mengine.utils.log_utils import logging_deco
from src.mengine.implementations.request_queue import RequestQueue
from src.mengine.enums.protocols import Protocol
from src.mengine.enums.http_version import Version


class ConcreteProcessManager(IProcessManager):

    def __init__(self, queue: RequestQueue, protocols: Protocol):
        self.queue = queue
        self.protocols = protocols

    @logging_deco
    def handle_connection(self, addr, conn):
        print(f"Handling connection from {addr}")
        try:
            chunks = []
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                chunks.append(data)
                if b"\r\n\r\n" in data:
                    break

            request = self.__parse_connection(conn, addr, chunks)
            response = self.generate_response(request)
            conn.sendall(response)

        except Exception as e:
            logging.exception(f"Unhandled exception on {e}", e)
        finally:
            conn.close()

    def generate_response(self, connection: IConnection):
        body = b"test for now"
        headers = [
            f"{connection.get_version().value} 200 OK".encode(),
            b"Content-Type: text/plain",
            b"Content-Length: " + str(len(body)).encode(),
            b"Connection: close",
        ]
        response = b"\r\n".join(headers) + b"\r\n\r\n" + body
        return response

    def __parse_connection(self, conn, addr, data):
        processed_payload = []
        for byte_chunk in data:
            decoded = byte_chunk.decode().split("\r\n")
            processed_payload.extend(decoded)

        length = len(processed_payload[0])

        if length == 0:
            return HTTPException

        if length >= 3:
            header_protocol, path, version = (processed_payload[0].split(" "))

            # Constructing the connection
            try:
                new_connection = ConcreteConnection(
                    addr, processed_payload)
                new_connection.set_method(Protocol(header_protocol))
                new_connection.set_version(Version(version))
                self.queue.enque(new_connection)

                print("Finished processing")
            except ValidationError as error:
                logging.error("Caught error when parsing payload %s", error)
        else:
            raise HTTPException
        return new_connection
