from src.mengine.interfaces.i_connection_manager import IConnectionManager
from src.mengine.interfaces.i_process_manager import IProcessManager
from src.mengine.interfaces.i_connection import Connection
from src.mengine.implementations.connection import ConcreteConnection
import socket


# Should handle and manage incomming connections
class ConnectionManager(IConnectionManager):
    #hack for now and this is class attributes
    ip = '127.0.0.1'
    port = 8084
    def __init__(self, process_manager: IProcessManager):
        self.process_manager = process_manager

    def start_up(self):
        return self.listen()

# I'm using the entire fucking tcp API call stack. LET this class only handle networking
    def listen(self) -> socket:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            s.listen(1)
            conn, addr = s.accept()
            print(f"delegating to process manager", conn, addr)
            self.process_manager.handle_connection(addr, conn)
