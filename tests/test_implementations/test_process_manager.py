import pytest
from unittest.mock import patch, MagicMock

from src.mengine.enums.protocols import Protocol
from src.mengine.implementations.process_manager import ConcreteProcessManager
from src.mengine.implementations.request_queue import RequestQueue
from tests.test_implementations.test_request_queue import mock_connection


@pytest.fixture
def stub_request_queue():
    return RequestQueue()

@pytest.fixture
def stub_protocol():
    return Protocol

class TestConcreteProcessManager:

    def test_handle_connection(self, stub_request_queue, stub_protocol):
        mock_connection = MagicMock()
        mock_connection.recv.return_value = b"GET / HTTP/1.1\r\n\r\n"
        test_class_instance = ConcreteProcessManager(stub_request_queue, stub_protocol)

        test_class_instance.handle_connection('127.0.0.1', mock_connection)

        mock_connection.recv.assert_called_with(1024)
        # Very close to actual implementation need to make it more generic
        mock_connection.sendall.assert_called_with(b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 12\r\nConnection: close\r\n\r\ntest for now')

    def test_handle_connection_failed(self, stub_request_queue, stub_protocol):
        with pytest.raises(Exception) as excp_msg:
            mock_connection = MagicMock()
            mock_connection.recv.return_value = b"BROKEN / HTTP/1.1\r\n\r\n"
            test_class_instance = ConcreteProcessManager(stub_request_queue, stub_protocol)

            test_class_instance.handle_connection('127.0.0.1', mock_connection)

            assert excp_msg == "Unhandled exception on "


    def test_generate_response(self, stub_request_queue, stub_protocol):
        structure = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 12\r\nConnection: close\r\n\r\ntest for now"

        mock_con = MagicMock()
        mock_con.get_version.return_value.value = "HTTP/1.1"

        test_class_instance = ConcreteProcessManager(stub_request_queue, stub_protocol)

        result = test_class_instance.generate_response(mock_con)
        assert result == structure
