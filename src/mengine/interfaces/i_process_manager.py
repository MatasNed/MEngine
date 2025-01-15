from abc import ABC, abstractmethod
from src.mengine.interfaces.i_connection import IConnection


class IProcessManager(ABC):

    @abstractmethod
    def handle_connection(self):
        pass

    @abstractmethod
    def generate_response(self, connection: IConnection):
        pass
