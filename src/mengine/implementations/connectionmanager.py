from src.mengine.interfaces.i_connection_manager import IConnectionManager
from src.mengine.interfaces.i_process_manager import ProcessManager
from src.mengine.interfaces.i_connection import Connection
from src.mengine.implementations.connection import ConcreteConnection
import socket


# Should handle and manage incomming connections
class ConnectionManager(IConnectionManager):
    #hack for now
    ip = '127.0.0.1'
    port = 8084
    def __init__(self):
        pass

    def start_up(self):
        return self.listen()

    def process_connection(self, connection: Connection):
        return connection

    def listen(self) -> socket:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                processs_con = self.process_connection(ConcreteConnection(addr, 's', conn.recv(1024))
                                                       )
            print(processs_con.get_payload(), processs_con.get_requester_ip())
