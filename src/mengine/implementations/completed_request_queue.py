from collections import deque
from time import monotonic

from src.mengine.interfaces.i_completed_request_queue import ICompletedRequestedQueue


class CompletedRequestQueue(ICompletedRequestedQueue):

    def __init__(self, timeout: int):
        self.queue = deque([])
        self.dlq = deque([])
        self.timeout = timeout
        self.completed_requests = set()

    def enque(self, request):
        self.__purge()
        time = monotonic()
        self.queue.append((request, time))

    def dequeu(self):
        self.__purge()

        while self.queue:
            request, timestamp, completed = self.queue.popleft()
            if completed:
                self.completed_requests.remove(request)
                return request
            else:
                self.queue.append((request, timestamp))
        return None

    def size(self):
        return len(self.queue)

    def mark_completed_request(self, request):
        self.completed_requests.add(request)

    # Would a heap be faster?
    def __purge(self):
        current_time = monotonic()

        while self.queue and current_time - self.queue[0][1] > self.timeout:
            request, _ = self.queue.popleft()
            self.dlq.append(request)

