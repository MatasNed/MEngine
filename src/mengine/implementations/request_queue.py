from src.mengine.interfaces.i_request_queue import IRequestQueue
from src.mengine.interfaces.i_connection import IConnection
from collections import deque
"""
A more interesting approach would be to implement thread-safe queue on my own? Future TODO?
"""


class RequestQueue(IRequestQueue):

    def __init__(self):
        self.queue = deque([])

    def enque(self, request: IConnection):
        self.queue.append(request)

    def dequeu(self):
        return self.queue.popleft()

    def size(self):
        return len(self.queue)
