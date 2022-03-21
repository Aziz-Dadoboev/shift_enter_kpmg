import unittest
import requests

from task_one import parse


class TestSomething(unittest.TestCase):

    def setUp(self):
        self.URL_TEMPLATE = "https://zakupki.gov.ru/epz/order/extendedsearch/results.html"

    def test_url(self):
        status = requests.get(self.URL_TEMPLATE).status_code
        self.assertEqual(status, 200, 'Status code is not equal 200 — problem in loading site')

    def test_values(self):
        self.assertGreater(len(parse(self.URL_TEMPLATE)), 0, 'Result list is EMPTY')


if __name__ == '__main__':
    unittest.main()
