import unittest

from manager import Manager  

class TestManager(unittest.TestCase):
  def test_set_name(self):
    manager = Manager("John", "password")
    self.assertEqual(manager.name_of_owner, "John")

  def test_get_name(self):
    manager = Manager("John", "password")
    self.assertEqual(manager.name_of_owner, "John")

  def test_set_password(self):
    manager = Manager("John", "password")
    self.assertEqual(manager.password, "password")

  def test_get_password(self):
    manager = Manager("John", "password")
    self.assertEqual(manager.password, "password")

if __name__ == '__main__':
  unittest.main()