import unittest
import requests

from flask import request

class ApiTest(unittest.TestCase):
  API_URL = 'http://localhost:3001'

  def test_1_check_on(self):
    response = requests.get(self.API_URL)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response._content.decode(), 'Wellcome')

if __name__ == '__main__':
  unittest.main()