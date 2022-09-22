import re
from django.test import TestCase, Client

# Create your tests here.
from django.test import TestCase, Client

# Create your tests here.
class MyWatchListTest(TestCase):
    def test_html(self):
        response = Client().get('/mywatchlist/html/')
        res = self.assertEqual(response.status_code, 200)
        return res
    
    def test_xml(self):
        response = Client().get('/mywatchlist/xml/')
        res = self.assertEqual(response.status_code, 200)
        return res
    
    def test_json(self):
        response = Client().get('/mywatchlist/json/')
        res = self.assertEqual(response.status_code, 200)
        return res