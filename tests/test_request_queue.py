""" This is a testing suite for RequestQueue class """
import pytest

from src.mengine.implementations.connection import ConcreteConnection
from src.mengine.implementations.request_queue import RequestQueue


@pytest.fixture(scope='class')
def mock_reqest_queue():
    """ Creates a RequestQueue instance for all test cases"""
    return RequestQueue()


@pytest.fixture(scope='class')
def mock_connection():
    """ Creates a Connection instance for test cases """
    return ConcreteConnection(requester_ip="localhost", payload=b'123')


class TestRequestQueue:
    """
        Test suite for the RequestQueue class to verify its queuing functionality.

        This class contains unit tests that cover the basic behaviors of a queue,
        ensuring that connections can be enqueued, dequeued, and that the size of
        the queue is accurately tracked.

    """

    def test_enque_adds_connection_to_queue(self, mock_reqest_queue,
                                            mock_connection):
        initial_size = mock_reqest_queue.size()
        mock_reqest_queue.enque(mock_connection)
        assert mock_reqest_queue.size() == initial_size + 1
        assert mock_reqest_queue.queue[-1] == mock_connection

    def test_deque_removes_connection_from_queue(self, mock_reqest_queue,
                                                 mock_connection):
        mock_reqest_queue.enque(mock_connection)
        initial_size = mock_reqest_queue.size()
        dequeued_connection = mock_reqest_queue.dequeu()
        assert dequeued_connection == mock_connection
        assert mock_reqest_queue.size() == initial_size - 1

    def test_size_of_queue(self, mock_reqest_queue, mock_connection):
        conn_1 = mock_connection
        conn_2 = mock_connection

        initial_size = mock_reqest_queue.size()

        assert mock_reqest_queue.size() == initial_size
        mock_reqest_queue.enque(conn_1)
        mock_reqest_queue.enque(conn_2)
        assert mock_reqest_queue.size() == initial_size + 2
