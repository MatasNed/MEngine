import logging
import socket
import threading

from src.mengine.interfaces.i_connection_manager import IConnectionManager
from src.mengine.interfaces.i_process_manager import IProcessManager
from src.mengine.utils.log_utils import logging_deco


# Should handle and manage incomming connections
class ConnectionManager(IConnectionManager):
    #hack for now and this is class attributes
    ip = '127.0.0.1'
    port = 8096
    max_threads_on_cpu = 2784
    """ macOs equivalent of linux /proc/sys/kernel/threads-max
    $ sysctl -a | grep maxproc
        kern.maxproc: 4176
        kern.maxprocperuid: 2784
    """

    def __init__(self, process_manager: IProcessManager):
        self.process_manager = process_manager

    def start_up(self):
        return self.listen()

    @logging_deco
    def listen(self) -> socket:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            s.listen(self.max_threads_on_cpu)

            """
            This manages overall process thread count not individual worker count
            Hitting max thread limit will throw Runtime/OSErrors considere handling this differently 
            """

            while threading.activeCount() < self.max_threads_on_cpu:
                if threading.activeCount() + 10 == self.max_threads_on_cpu:
                    logging.warning("Close to thread limit for the system")
                conn, addr = s.accept()
                worker = threading.Thread(
                    target=self.process_manager.handle_connection,
                    args=(addr, conn),
                    daemon=False)
                worker.start()
