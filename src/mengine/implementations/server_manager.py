from src.mengine.interfaces.i_connection_manager import IConnectionManager


class ServerManager:
    def __init__(self, conn_manager: IConnectionManager, ip="127.0.0.1", port=8084):
        self.ip = ip
        self.port = port
        self.conn_manager = conn_manager

    def start_up_conn(self) -> IConnectionManager:
        return self.conn_manager.start_up()
