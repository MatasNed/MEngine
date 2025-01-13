from socket import socket

from src.mengine.implementations.connection import ConcreteConnection
from src.mengine.interfaces.i_connection import Connection
from src.mengine.interfaces.i_process_manager import IProcessManager

class ConcreteProcessManager(IProcessManager):
    def __init__(self):
        pass

    def handle_connection(self, addr, conn):
        with conn:
            data = conn.recv(1024)

            c_conn = ConcreteConnection(addr, data)

            self.process_connection(c_conn)

    def process_connection(self, connection: ConcreteConnection):
        print("YESS", connection.payload)
