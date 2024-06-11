import typing
from abc import ABC

from process_manager import ProcessManager
from connection import ConcreteConnection
from abstractconnection import Connection
from enum import Enum
import socket


class ServerManager(ProcessManager):
    def __init__(self, ip="127.0.0.1", port=8084):
        self.ip = ip
        self.port = port

    # It makes no sense for the ServerManager to also handle the connectiosn
    # The connection manager should handle eand delegate connections. So ServerManager implementing ProcessManager is stupid
    # Need to create 1 connmanager which will handle the conns, while server manager handles server setup.
    def process_connection(self, connection: Connection) -> Connection:
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
