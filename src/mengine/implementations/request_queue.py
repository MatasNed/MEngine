from src.mengine.interfaces.i_request_queue import IRequestQueue
from src.mengine.interfaces.i_connection import Connection
from collections import deque


class RequestQueue(IRequestQueue):

    def __init__(self):
        self.queue = deque([])

    def enque(self, request: Connection):
        self.queue.append(request)

    def dequeu(self):
        return self.queue.popleft()

    def size(self):
        return len(self.queue)
