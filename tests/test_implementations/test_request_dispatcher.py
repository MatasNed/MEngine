import pytest
from unittest.mock import patch, MagicMock

from src.mengine.exceptions.exceptions import HTTPException
from src.mengine.implementations.request_dispatcher import RequestDispatcher
from src.mengine.implementations.request_queue import RequestQueue


class TestRequestDispatcher:
    # DP mocking
    @patch('src.mengine.implementations.request_dispatcher.socket.socket')
    def test_request_dispatcher(self, mock_socket):
        # Instanciating the mock
        mock_socket_instance = mock_socket.return_value

        # Setup
        mock_r_queue = RequestQueue()
        mock_conn = MagicMock()
        mock_r_queue.enque(mock_conn)
        mock_conn.get_version.return_value.value = "HTTP/1.1"
        mock_conn.get_method.return_value.value = "GET"
        mock_conn.get_payload.return_value = b"some payload"
        request_dispatch = RequestDispatcher(mock_r_queue)

        # Test
        request_dispatch.dispatch_request()

        # exepected
        mock_socket_instance.connect.assert_called_once_with(("0.0.0.0", 9000))

        expected = (
            b"GET / HTTP/1.1\r\n"
            b"Content-Type: text/plain\r\n"
            b"Content-Length: b'some payload'\r\n"
            b"\r\n"
        )
        mock_socket_instance.send.assert_called_once_with(expected)

    @patch('src.mengine.implementations.request_dispatcher.socket.socket')
    def test_request_dispatcher_broken(self, mock_socket):
        with pytest.raises(HTTPException):
            mock_r_queue = RequestQueue()
            mock_conn = MagicMock()
            mock_r_queue.enque(mock_conn)
            request_dispatch = RequestDispatcher(mock_r_queue)
            request_dispatch.dispatch_request()