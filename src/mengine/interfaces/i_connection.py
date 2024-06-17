from abc import ABC, abstractmethod


class Connection(ABC):
    @abstractmethod
    def get_requester_ip(self):
        pass

    @abstractmethod
    def get_path(self):
        pass

    @abstractmethod
    def get_payload(self):
        pass