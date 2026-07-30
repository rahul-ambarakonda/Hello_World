
import unittest
import http.server
import socketserver
import os
import sys

# Add the parent directory to the path to import server.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hello_world_app import server

class TestServerConfiguration(unittest.TestCase):

    def test_port_is_8000(self):
        self.assertEqual(server.PORT, 8000, "Server should listen on port 8000")

    def test_directory_is_static(self):
        self.assertEqual(server.DIRECTORY, "static", "Server should serve from 'static' directory")

    def test_handler_uses_correct_directory(self):
        # We can't easily instantiate and test the SimpleHTTPRequestHandler's
        # internal directory setting without a live server or extensive mocking.
        # This test checks the configuration variable that the handler uses.
        # More advanced testing would require integration tests or more complex mocking.
        # For a simple unit test, verifying the DIRECTORY constant is sufficient.
        self.assertEqual(server.Handler.directory, server.DIRECTORY, "Handler should be configured with the correct directory")

if __name__ == '__main__':
    unittest.main()
