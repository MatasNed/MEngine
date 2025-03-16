from unittest.async_case import IsolatedAsyncioTestCase
from unittest.mock import MagicMock, patch
from src.mengine.implementations.request_queue_consumer_daemon import RequestQueueConsumerDaemon


class TestRequestQueueConsumerDaemon(IsolatedAsyncioTestCase):

    # Patch requires argument to the function to be passed
    @patch('asyncio.sleep')
    async def test_consume(self, mock_sleep):
        # Mocking the queue, not using AsyncMock as queue itself is sync
        mock_queue = MagicMock()

        # Instantiation
        daemon = RequestQueueConsumerDaemon(mock_queue, 0)

        # Sets false first followed by a True
        daemon.stop_event.is_set = MagicMock(side_effect=[False, True])

        # Actual logic
        await daemon.consume()

        # Expectation
        assert mock_queue.dispatch_request.called

    def test_stop(self):
        # Instance
        instance = RequestQueueConsumerDaemon(MagicMock(), 0)

        # Logic
        instance.stop()

        # Actually is changed
        assert instance.stop_event.is_set()