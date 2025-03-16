from abc import abstractmethod

from src.mengine.interfaces.i_request_queue import IRequestQueue


class ICompletedRequestedQueue(IRequestQueue):

    @abstractmethod
    def mark_completed_request(self, request):
        """ Mark Request as Completed """
        pass