from abc import ABC, abstractmethod
from connection import Connection

class ProcessManager(ABC):
    @abstractmethod
    def process_connection(self, connection: Connection):
        pass