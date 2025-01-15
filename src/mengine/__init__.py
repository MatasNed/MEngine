from src.mengine.implementations import server_manager
from src.mengine.implementations import connectionmanager
from src.mengine.implementations import process_manager
from src.mengine.implementations import request_queue
from src.mengine.implementations import request_dispatcher
from src.mengine.enums import protocols


def main():
    # Initialize and run your class
    q = request_queue.RequestQueue()
    proc_mg = process_manager.ConcreteProcessManager(q, protocols.Protocol)
    disp = request_dispatcher.RequestDispatcher(q)
    con_mg = connectionmanager.ConnectionManager(proc_mg)
    instance = server_manager.ServerManager(con_mg, disp)

    instance.start_up_conn()
    instance.dispatcher_daemon()


# Check if the script is being run directly
if __name__ == "__main__":
    main()
