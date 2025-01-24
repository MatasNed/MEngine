from abc import ABC, abstractmethod


class IConnection(ABC):

    @abstractmethod
    def get_requester_ip(self):
        pass

    @abstractmethod
    def get_payload(self):
        pass
