from src.mengine.interfaces.i_connection_manager import IConnectionManager
from src.mengine.interfaces.i_process_manager import IProcessManager
import socket
from src.mengine.utils.log_utils import logging_deco
import threading


# Should handle and manage incomming connections
class ConnectionManager(IConnectionManager):
    #hack for now and this is class attributes
    ip = '127.0.0.1'
    port = 8095

    def __init__(self, process_manager: IProcessManager):
        self.process_manager = process_manager

    def start_up(self):
        return self.listen()

    # This is awful
    @logging_deco
    def listen(self) -> socket:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            s.listen(5)
            i = 0
            while i < 2:
                conn, addr = s.accept()
                t = threading.Thread(
                    target=self.process_manager.handle_connection,
                    args=(addr, conn),
                    daemon=False)
                t.start()
                i += 1
