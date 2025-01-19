import logging
from socket import socket

from src.mengine.implementations.connection import ConcreteConnection
from src.mengine.interfaces.i_process_manager import IProcessManager
from src.mengine.utils.log_utils import logging_deco
from src.mengine.implementations.request_queue import RequestQueue
from src.mengine.enums.protocols import Protocol


class ConcreteProcessManager(IProcessManager):

    def __init__(self, queue: RequestQueue, protocols: Protocol):
        self.queue = queue
        self.protocols = protocols

    @logging_deco
    def handle_connection(self, addr, conn):
        print(f"Handling connection from {addr}")
        with conn:
            data = conn.recv(1024)

            c_conn = ConcreteConnection(addr, data)

            self.process_connection(c_conn)
            self.__parse_connection(c_conn)

    def process_connection(self, connection: ConcreteConnection):
        try:
            decoded_str = connection.get_payload().decode().split(" ")

            for val in range(2):
                if decoded_str[val] == 'GET':
                    connection.set_method(self.protocols.GET)
                    self.queue.enque(connection)
                elif decoded_str[val] == 'POST':
                    connection.set_method(self.protocols.POST)
                    self.queue.enque(connection)
        except ValueError:
            logging.error("The protocol could not be processed")

    # useless
    def __parse_connection(self, connection: ConcreteConnection):

        print(connection.get_payload().decode().split(" "))
