from unittest import TestCase
from unittest.mock import patch, call

from src.question2 import task_completed


class TestQuestion2(TestCase):
    def setUp(self):
        self.maxDiff = None

    @patch('src.notify.send_email')
    def test_task_completed_notify_admin(self, mock_send_email):
        task_completed(12)
        expected_calls = [
            call.send_email('xanderson@example.org', 'supervisor-task-completed'),
            call.send_email('tinachristensen@example.com', 'supervisor-task-completed'),
            call.send_email('agarcia@example.org', 'supervisor-task-completed'),
            call.send_email('stephaniekrause@example.com', 'supervisor-task-completed'),
            call.send_email('kelly09@example.net', 'supervisor-task-completed')
        ]

        mock_send_email.assert_has_calls(expected_calls)

    @patch('src.notify.send_email')
    def test_task_complete_notify_next_user(self, mock_send_email):
        task_completed(15)

        mock_send_email.assert_called_with('agarcia@example.org', 'worker-task-ready')
