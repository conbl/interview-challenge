from unittest import TestCase

from src.question1 import filter_tasks

from results.question1 import question1_test1, question1_test2, question1_test3, question1_test4


class TestQuestion1(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_filter_tasks_by_assignment(self):
        self.assertEqual({x['id'] for x in question1_test1}, {x['id'] for x in filter_tasks({"assigned_user_id": [22, 34, 41]})})

    def test_filter_tasks_by_home(self):
        self.assertEqual({x['id'] for x in question1_test2}, {x['id'] for x in filter_tasks({'home_id': [37, 8, 41, 48, 75]})})

    def test_filter_tasks_by_reservation_checkin(self):
        self.assertEqual({x['id'] for x in question1_test3}, {x['id'] for x in filter_tasks({'reservation': ['checkin']})})

    def test_filter_tasks_by_reservation_checkout_and_unassigned(self):
        self.assertEqual(
            {x['id'] for x in question1_test4},
            {x['id'] for x in filter_tasks({'reservation': ['checkout'],'assigned_user_id': None})}
        )
