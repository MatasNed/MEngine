import logging
import socket

from src.mengine.exceptions.exceptions import HTTPException
from src.mengine.exceptions.exceptions import ValidationError
from src.mengine.implementations.completed_request_queue import CompletedRequestQueue
from src.mengine.interfaces.i_request_dispatcher import IRequestDispatcher
from src.mengine.implementations.request_queue import RequestQueue
from src.mengine.interfaces.i_socket_handler import ISocketHandler
from src.mengine.validators.http_validator import HTTPValidator
from src.mengine.implementations.socket_handler import SocketHandler


class RequestDispatcher(IRequestDispatcher):
    # TODO fix
    host = "0.0.0.0"
    port = 9000

    def __init__(self, dispatch_queue: RequestQueue, socket_handler: ISocketHandler):
        self.dispatch_queue = dispatch_queue
        self.socket_handler = socket_handler

    def dispatch_request(self):
        try:

            while self.dispatch_queue.size() != 0:
                message = self.dispatch_queue.dequeu()

                self.socket_handler = SocketHandler(message.get_requester_ip_and_port(),
                                                    message.get_response_sock,
                                                    self.host,
                                                    self.port)


                backend_response = self.socket_handler.send_request(message)

                # Send to the one that is encapsulated in the IP that's who needs the response,
                # but isn't the conn closed already?
                # Someone must be blokcing the waiting thread or else we terminate the conn without waiting for the response

                E#nqueue to completed requests
                # CompletedRequestQueue.enque(backend_response)
                # CompletedRequestQueue.mark_completed_request(backend_response)
                print(backend_response)
        except ValidationError as error:
            logging.exception("Validation error on: %s", error)
            raise HTTPException("Invalid HTTP data") from error

