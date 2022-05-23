import unittest
import requests
import json


class ApiTest(unittest.TestCase):
  API_URL = 'http://localhost:3001'

  def test_1_check_on(self):
    response = requests.get(self.API_URL)
    self.assertEqual(response.status_code, 200)
    self.assertDictEqual(json.loads(response.content), {'hello': 'Wellcome'})

  def test_2_check_getall(self):
    response = requests.get('{}/getall'.format(self.API_URL))
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(json.loads(response.content)), 1126) # 1126 items in results of api

  def test_3_check_search_null(self):
    response = requests.get('{}/search/nonamepoke'.format(self.API_URL))
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(json.loads(response.content)), 0) # 0 items in results of api

if __name__ == '__main__':
  unittest.main()