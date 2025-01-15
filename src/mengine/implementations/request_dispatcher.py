from urllib.error import HTTPError

from src.mengine.interfaces.i_request_dispatcher import IRequestDispatcher
from src.mengine.implementations.request_queue import RequestQueue
import socket


class RequestDispatcher(IRequestDispatcher):
    # TODO fix
    host = "0.0.0.0"
    port = 9000

    def __init__(self, dispatch_queue: RequestQueue):
        self.dispatch_queue = dispatch_queue

    def dispatch_request(self):
        try:
            client_socket = socket.socket()
            client_socket.connect((self.host, self.port))

            while self.dispatch_queue.size() != 0:
                message = self.dispatch_queue.dequeu()
                payload = message.get_payload()
                version = message.get_version()
                method = message.get_method()
                headers = [
                    f"{method} / {version}".encode(),
                    b"Content-Type: text/plain",
                    b"Content-Length: " + str(len(payload)).encode(),
                ]
                response = b"\r\n".join(headers) + b"\r\n\r\n"
                client_socket.send(response)
        except HTTPError:
            print("HTTP Error from Dispatch")
