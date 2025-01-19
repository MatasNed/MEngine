from abc import ABC, abstractmethod


class IConnectionManager(ABC):

    @abstractmethod
    def listen(self):
        pass

    @abstractmethod
    def start_up(self):
        pass
