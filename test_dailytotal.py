import unittest

from dailytotal import DailyTotal

class TestDailyTotal(unittest.TestCase):

    def test_set_date(self):
        daily_total = DailyTotal()
        daily_total.set_date("2023-04-01")
        self.assertEqual(daily_total.get_date(), "2023-04-01")

    def test_get_date(self):
        daily_total = DailyTotal()
        daily_total.set_date("2023-04-01")
        self.assertEqual(daily_total.get_date(), "2023-04-01")

    def test_set_total(self):
        daily_total = DailyTotal()
        daily_total.set_total(100.0)
        self.assertEqual(daily_total.get_total(), 100.0)

    def test_get_total(self):
       daily_total = DailyTotal()
       daily_total.set_total(10.0)
       self.assertEqual(daily_total.get_total(), 10.0)


if __name__ == '__main__':
    unittest.main()