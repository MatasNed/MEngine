import logging
import socket

from src.mengine.exceptions.exceptions import HTTPException
from src.mengine.interfaces.i_request_dispatcher import IRequestDispatcher
from src.mengine.implementations.request_queue import RequestQueue
from src.mengine.validtors.http_validator import HTTPValidator


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
                payload = HTTPValidator.validate_payload(str(message.get_payload()).encode())
                version = HTTPValidator.validate_version(message.get_version().value)
                method = HTTPValidator.validate_method(message.get_method().value)
                headers = [
                    f"{method} / {version}".encode(),
                    b"Content-Type: text/plain",
                    b"Content-Length: " + payload,
                ]
                response = b"\r\n".join(headers) + b"\r\n\r\n"
                client_socket.send(response)
        except HTTPException as error:
            logging.exception("HTTPException has occured", error)

