from abc import ABC, abstractmethod


class IRequestDispatcher(ABC):

    @abstractmethod
    def dispatch_request(self):
        pass
