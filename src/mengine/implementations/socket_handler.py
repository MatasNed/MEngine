import logging
from socket import socket

from src.mengine.interfaces.i_connection import IConnection
from src.mengine.interfaces.i_socket_handler import ISocketHandler
from src.mengine.exceptions.exceptions import HTTPException, ValidationError
from src.mengine.implementations.concrete_connection import ConcreteConnection
from src.mengine.enums.protocols import Protocol
from src.mengine.enums.http_version import Version


class SocketHandler(ISocketHandler):

    def __init__(self, client_addr, client_socket, backend_host, backend_port):
        self.addr = client_addr
        self.conn = client_socket
        self.backend_host = backend_host
        self.backend_port = backend_port
        self.backend_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def read_tcp_conn(self, client_addr, client_socket):
        try:
            chunks = []

            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                chunks.append(data)
                if b"\r\n\r\n" in data:
                    break

            new_request = self.__parse_connection(client_addr, chunks, client_socket)
            return new_request

        except Exception as e:
            logging.exception(f"Unhandled exception on {client_addr}: {e}", e)


    def __parse_connection(self, addr, data, sock):
        processed_payload = []
        for byte_chunk in data:
            decoded = byte_chunk.decode().split("\r\n")
            processed_payload.extend(decoded)


        if not processed_payload or not processed_payload[0]:
            raise HTTPException("Malformed headers")


        try:
            header_protocol, path, version = (processed_payload[0].split(" "))
        except ValueError:
            raise HTTPException("Error processing headers")


        # Constructing the connection
        try:
            new_connection = ConcreteConnection(
                addr, processed_payload, sock)
            new_connection.set_method(Protocol(header_protocol))
            new_connection.set_version(Version(version))

            print("Finished processing")
        except ValidationError as error:
            logging.error("Caught error when parsing payload %s", error)
            raise HTTPException("Invalid request") from error
        return new_connection

    def generate_response(self, connection: IConnection, response_code):
        headers = [
            f"{connection.get_version().value} {response_code}".encode(),
            b"Content-Type: text/plain",
            b"Content-Length: " + str(len(connection.payload)).encode(),
            b"Connection: close",
        ]
        response = b"\r\n".join(headers) + b"\r\n\r\n" + connection.get_payload().encode()
        return response

    def send_request(self, connection: IConnection) -> IConnection:
        self.backend_conn.settimeout(10)

        headers = [
            f"{connection.get_method()} {connection.get_path()} {connection.get_version()}".encode(),
            b"Content-Type: text/plain",
            b"Content-Length: " + str(len(connection.get_payload())).encode(),
        ]
        request = b"\r\n".join(headers) + b"\r\n\r\n" + connection.get_payload().encode()

        try:
            self.backend_conn.connect((self.backend_host, self.backend_port))
            self.backend_conn.send(request)

            result = self.read_tcp_conn(self.backend_host, self.backend_conn)
            return result
        except TimeoutError as e:
            raise TimeoutError(e)
        finally:
            self.backend_conn.close()