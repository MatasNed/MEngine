from time import sleep

from src.mengine.interfaces.i_connection_manager import IConnectionManager
from src.mengine.utils.log_utils import logging_deco
from src.mengine.implementations.request_dispatcher import RequestDispatcher


class ServerManager:

    def __init__(self, conn_manager: IConnectionManager,
                 dis: RequestDispatcher):
        self.conn_manager = conn_manager
        self.dis = dis

    @logging_deco
    def start_up_conn(self) -> IConnectionManager:
        return self.conn_manager.start_up()

    # Periodically dispatch queued requests
    # TODO fix this mess
    def dispatcher_daemon(self):
        sleep(5)
        n = 5
        i = 0
        while i < n:
            self.dis.dispatch_request()
            i += 1
