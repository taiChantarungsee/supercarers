import unittest
from main import app
   
class TestCase(unittest.TestCase):

    def setUp(self): 
        self.app = app
        self.client = app.test_client()
        self.client.testing = True

    def test_weather_overview(self):
    	response = self.client.get('/weather/london/20180329/1200/')
    	self.assertEqual(response.status_code, 200)
    	self.assertIn(b'"humidity": "91%"',response.data)

    def test_weather_property(self):
    	response = self.client.get('/weather/london/20180329/1200/temperature/')
    	self.assertEqual(response.status_code, 200)
    	self.assertIn(b'"temperature": "139c"',response.data)

    def test_wrong_date(self):
        response = self.client.get('/weather/london/20120329/1200/temperature/')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'"status": "error"',response.data)
              
if __name__ == "__main__":
    unittest.main()