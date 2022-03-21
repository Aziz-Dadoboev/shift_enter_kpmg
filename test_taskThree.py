import unittest
import sqlite3
from task_three import createTable


class TestSomething(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(r'cards.db')
        # self.cur = createTable()
        self.cur = createTable()

    def test_db(self):
        result = self.cur.fetchall()
        self.assertIsNot(result, 0, 'Database is empty')

    def test_value(self):
        result = self.cur.fetchmany(3)
        self.assertGreater(int(result[0][0]), 0, 'First value is empty')
        self.assertGreater(int(result[0][1]), 0, 'First value is empty')
        self.assertGreater(int(result[1][0]), 0, 'Second value is empty')
        self.assertGreater(int(result[1][1]), 0, 'Second value is empty')
        self.assertGreater(int(result[2][0]), 0, 'Third value is empty')
        self.assertGreater(int(result[2][1]), 0, 'Third value is empty')


# cur.execute("SELECT * FROM cards;")
# one_result = cur.fetchone()
# print(one_result)

if __name__ == '__main__':
    unittest.main()
