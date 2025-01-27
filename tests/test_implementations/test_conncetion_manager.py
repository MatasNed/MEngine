from unittest.mock import patch, MagicMock
from src.mengine.implementations.connection_manager import ConnectionManager


class TestConnectionManagerLoop:
    @patch('src.mengine.implementations.connection_manager.threading.Thread')
    @patch('src.mengine.implementations.connection_manager.threading.activeCount')
    @patch('src.mengine.implementations.connection_manager.socket.socket')
    def test_listen(self, mock_socket_constructor,mock_active_count, mock_thread):
        mock_process_manager = MagicMock()
        conn_mgr = ConnectionManager(process_manager=mock_process_manager)

        # Necessary due to with context-manager
        mocked_socket_instance = mock_socket_constructor.return_value.__enter__.return_value

        mock_active_count.side_effect = [2783, 2783, 2784]

        fake_conn = MagicMock()
        fake_addr = ('127.0.0.1', 12345)
        mocked_socket_instance.accept.return_value = (fake_conn, fake_addr)

        # Test
        conn_mgr.listen()

        # Expect
        mocked_socket_instance.bind.assert_called_once_with(('127.0.0.1', 8096))
        mocked_socket_instance.listen.assert_called_once_with(2784)

        mocked_socket_instance.accept.assert_called_once()

        # Based on implementation check how many threads
        mock_thread.assert_called_once()

        # Instanciate
        mock_thread_instance = mock_thread.return_value
        mock_thread_instance.start.assert_called_once()