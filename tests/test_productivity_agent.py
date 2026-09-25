import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestProductivityAgent(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_task_extraction_and_briefing(self):
        text = "1. Fix critical production memory leak ASAP\n2. Review Q4 hiring plan\n3. Email investor update today"
        res = self.client.post("/daily-briefing", json={"raw_text": text})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["tasks_count"], 3)
        self.assertGreaterEqual(len(data["high_priority_tasks"]), 2)

if __name__ == "__main__":
    unittest.main()
