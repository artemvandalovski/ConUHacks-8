import unittest
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch
from app.routes.schedule_routes import app


class ScheduleRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_schedule_success(self):
        with patch(
            "app.routes.schedule_routes.get_schedule_by_date"
        ) as mock_get_schedule_by_date:
            mock_get_schedule_by_date.return_value = {
                "date": "2022-01-01",
                "event": "ConUHacks",
            }
            response = self.app.get("/schedule/2022-01-01")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                response.json, {"date": "2022-01-01", "event": "ConUHacks"}
            )

    def test_get_schedule_not_found(self):
        with patch(
            "app.routes.schedule_routes.get_schedule_by_date"
        ) as mock_get_schedule_by_date:
            mock_get_schedule_by_date.return_value = None
            response = self.app.get("/schedule/2022-01-01")
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.json, {"error": "Schedule not found"})


if __name__ == "__main__":
    unittest.main()
