from abc import ABC, abstractmethod

class ISocketHandler(ABC):

    @abstractmethod
    def read_tcp_conn(self):
        pass

    @abstractmethod
    def generate_response(self):
        pass