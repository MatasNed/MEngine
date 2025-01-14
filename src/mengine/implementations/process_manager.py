from socket import socket

from src.mengine.implementations.connection import ConcreteConnection
from src.mengine.interfaces.i_process_manager import IProcessManager
from src.mengine.utils.log_utils import logging_deco

class ConcreteProcessManager(IProcessManager):
    def __init__(self):
        pass

    @logging_deco
    def handle_connection(self, addr, conn):
        with conn:
            data = conn.recv(1024)

            c_conn = ConcreteConnection(addr, data)

            self.process_connection(c_conn)

    def process_connection(self, connection: ConcreteConnection):
        print("YESS", connection.get_payload())
