import time
import threading

from src.mengine.implementations import server_manager
from src.mengine.implementations import connectionmanager
from src.mengine.implementations import process_manager
from src.mengine.implementations import request_queue
from src.mengine.implementations import request_dispatcher
from src.mengine.enums import protocols
from src.mengine.implementations import request_queue_consumer_daemon


def main():
    # Initialize and run your class
    q = request_queue.RequestQueue()
    proc_mg = process_manager.ConcreteProcessManager(q, protocols.Protocol)
    disp = request_dispatcher.RequestDispatcher(q)
    con_mg = connectionmanager.ConnectionManager(proc_mg)

    daemon = request_queue_consumer_daemon.RequestQueueConsumerDaemon(disp, 1)

    deamon_t = threading.Thread(target=daemon.consume, daemon=True)
    deamon_t.start()

    instance = server_manager.ServerManager(con_mg, disp)
    instance.start_up_conn()

    time.sleep(10)
    daemon.stop()
    deamon_t.join()


# Check if the script is being run directly
if __name__ == "__main__":
    main()
