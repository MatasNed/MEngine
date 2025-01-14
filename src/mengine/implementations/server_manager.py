from src.mengine.interfaces.i_connection_manager import IConnectionManager
from src.mengine.utils.log_utils import logging_deco
class ServerManager:
    def __init__(self, conn_manager: IConnectionManager):
        self.conn_manager = conn_manager

    @logging_deco
    def start_up_conn(self) -> IConnectionManager:
        return self.conn_manager.start_up()
