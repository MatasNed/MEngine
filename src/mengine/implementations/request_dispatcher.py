from urllib.error import HTTPError

from src.mengine.interfaces.i_request_dispatcher import IRequestDispatcher
from src.mengine.implementations.request_queue import RequestQueue
import socket


class RequestDispatcher(IRequestDispatcher):
    # temp hack
    # TODO fix
    host = "0.0.0.0"
    port = 9000

    def __init__(self, dispatch_queue: RequestQueue):
        self.dispatch_queue = dispatch_queue

    def dispatch_request(self):
        print('s')
        try:
            client_socket = socket.socket()
            client_socket.connect((self.host, self.port))
            print('s1')

            while self.dispatch_queue.size() != 0:
                message = self.dispatch_queue.dequeu()
                boo = client_socket.send(str(message).encode())
                # really?
        except HTTPError:
            print("HTTP Error from Dispatch")
