from abc import ABC, abstractmethod
from src.mengine.interfaces.i_connection import Connection


class ProcessManager(ABC):
    @abstractmethod
    def process_connection(self, connection: Connection):
        pass