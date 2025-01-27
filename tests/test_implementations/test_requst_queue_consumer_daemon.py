import threading
from unittest.mock import MagicMock
from src.mengine.implementations.request_queue_consumer_daemon import RequestQueueConsumerDaemon


class TestRequestQueueConsumerDaemon:

    def test_consume(self):
        # Mocking out the dependency
        mock_queue = MagicMock()

        # Instance of the tested class
        daemon = RequestQueueConsumerDaemon(mock_queue, timer=0.1)

        # Running on seprate thread or else while loop will block the thread
        running_on_seprate_thread = threading.Thread(target=daemon.consume)
        running_on_seprate_thread.start()

        # Stopping the daemon to terminate the blocking thread from the main
        daemon.stop()

        # Reaping the result
        running_on_seprate_thread.join()

        assert mock_queue.dispatch_request.called
