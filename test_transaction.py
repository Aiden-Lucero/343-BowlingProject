import unittest

from transaction import Transaction

class TestTransaction(unittest.TestCase):
  def test_set_name(self):
    transaction = Transaction()
    transaction.set_name("John")
    self.assertEqual(transaction.get_name(), "John")

  def test_get_name(self):
    transaction = Transaction()
    transaction.set_name("John")
    self.assertEqual(transaction.get_name(), "John")

  def test_set_start_time(self):
    transaction = Transaction()
    transaction.set_start_time(10)
    self.assertEqual(transaction.get_start_time(), 10)

  def test_set_lane_number(self):
    transaction = Transaction()
    transaction.set_lane_number(1)
    self.assertEqual(transaction.get_lane_number(), 1)

  def test_get_lane_number(self):
    transaction = Transaction()
    transaction.set_lane_number(1)
    self.assertEqual(transaction.get_lane_number(), 1)

  def test_get_start_time(self):
    transaction = Transaction()
    transaction.set_start_time(10)
    self.assertEqual(transaction.get_start_time(), 10)

  def test_set_end_time(self):
    transaction = Transaction()
    transaction.set_end_time(20)
    self.assertEqual(transaction.get_end_time(), 20)

  def test_get_end_time(self):
    transaction = Transaction()
    transaction.set_end_time(20)
    self.assertEqual(transaction.get_end_time(), 20)

  def test_set_date(self):
    transaction = Transaction()
    transaction.set_date("2023-04-01")
    self.assertEqual(transaction.get_date(), "2023-04-01")

  def test_get_date(self):
    transaction = Transaction()
    transaction.set_date("2023-04-01")
    self.assertEqual(transaction.get_date(), "2023-04-01")

if __name__ == '__main__':
  unittest.main()  
    