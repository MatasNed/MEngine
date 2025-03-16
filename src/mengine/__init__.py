import time
import threading
import asyncio

from src.mengine.implementations import server_manager
from src.mengine.implementations import connection_manager
from src.mengine.implementations import process_manager
from src.mengine.implementations import request_queue
from src.mengine.implementations import request_dispatcher
from src.mengine.enums import protocols
from src.mengine.implementations import request_queue_consumer_daemon


async def main():
    # Initialize and run your class
    q = request_queue.RequestQueue()
    proc_mg = process_manager.ConcreteProcessManager(q, protocols.Protocol)
    disp = request_dispatcher.RequestDispatcher(q)
    con_mg = connection_manager.ConnectionManager(proc_mg)

    daemon = request_queue_consumer_daemon.RequestQueueConsumerDaemon(disp, 1)
    asyncio.create_task(daemon.consume())

    instance = server_manager.ServerManager(con_mg, disp)

    # I have to move this listen() block call away from main thread to allow asyncio event loop to run
    await asyncio.to_thread(instance.start_up_conn)

    daemon.stop()



# Check if the script is being run directly
if __name__ == "__main__":
    asyncio.run(main())
