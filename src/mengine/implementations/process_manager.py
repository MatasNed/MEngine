import logging

from src.mengine.exceptions.exceptions import ValidationError, HTTPException
from src.mengine.implementations.concrete_connection import ConcreteConnection
from src.mengine.interfaces.i_connection import IConnection
from src.mengine.interfaces.i_process_manager import IProcessManager
from src.mengine.utils.log_utils import logging_deco
from src.mengine.implementations.request_queue import RequestQueue
from src.mengine.enums.protocols import Protocol
from src.mengine.enums.http_version import Version
from src.mengine.implementations.socket_handler import SocketHandler


class ConcreteProcessManager(IProcessManager):

    def __init__(self, queue: RequestQueue, protocols: Protocol):
        self.queue = queue
        self.protocols = protocols

    @logging_deco
    @logging_deco
    def handle_connection(self, addr, conn):
        print(f"Handling connection from {addr}")
        try:
            # Use SocketHandler instead of parsing manually
            socket_handler = SocketHandler(addr, conn)  # No need to pass backend_host and backend_port
            request = socket_handler.read_tcp_conn(addr, conn)

            # Enqueue the parsed request
            self.queue.enque(request)

            response = self.generate_response(request)
            conn.sendall(response)

        except Exception as e:
            logging.exception(f"Unhandled exception on {addr}: {e}", e)
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


