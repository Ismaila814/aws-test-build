import unittest
from app import sayhello

class TestApp(unittest.TestCase):
    def test_sayhello(self):
        self.assertEqual(sayhello(), "Hello, World!") 