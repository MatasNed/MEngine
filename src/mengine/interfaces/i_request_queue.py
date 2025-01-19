from abc import ABC, abstractmethod


class IRequestQueue(ABC):

    @abstractmethod
    def enque(self, request):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def dequeu(self):
        pass
