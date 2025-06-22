from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.

class ReportEndpointTest(TestCase):
    def setUp(self):
        # Use reverse() for URL resolution to avoid hard‐coding
        self.url = reverse('emissions-report')  
        self.client = Client()

    def test_report_returns_three_keys(self):
        response = self.client.get(self.url)
        # 1) status code
        self.assertEqual(response.status_code, 200)

        # 2) JSON payload
        data = response.json()
        expected_keys = {"total_tCO2e", "projects", "data_quality_pct"}
        self.assertEqual(set(data.keys()), expected_keys)