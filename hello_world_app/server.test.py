
import unittest
import os
import sys

# Ensure the directory containing server.py is in sys.path
sys.path.insert(0, os.path.dirname(__file__))
import server

class TestServerConfiguration(unittest.TestCase):

    def test_port_is_8000(self):
        self.assertEqual(server.PORT, 8000, "Server should listen on port 8000")

    def test_directory_is_static(self):
        self.assertEqual(server.DIRECTORY, "static", "Server should serve from 'static' directory")

if __name__ == '__main__':
    unittest.main()
