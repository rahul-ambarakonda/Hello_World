
import unittest
import os

class TestIndexHtml(unittest.TestCase):

    def setUp(self):
        self.html_path = os.path.join(os.path.dirname(__file__), 'index.html')
        with open(self.html_path, 'r') as f:
            self.html_content = f.read()

    def test_html5_boilerplate_present(self):
        self.assertIn('<!DOCTYPE html>', self.html_content)
        self.assertIn('<html lang="en">', self.html_content)
        self.assertIn('<head>', self.html_content)
        self.assertIn('<body>', self.html_content)
        self.assertIn('</head>', self.html_content)
        self.assertIn('</body>', self.html_content)
        self.assertIn('</html>', self.html_content)

    def test_h1_with_hello_world(self):
        self.assertIn('<h1>Hello World!</h1>', self.html_content)

    def test_css_linked(self):
        self.assertIn('<link rel="stylesheet" href="css/style.css">', self.html_content)

    def test_meta_charset_present(self):
        self.assertIn('<meta charset="UTF-8">', self.html_content)

    def test_meta_viewport_present(self):
        self.assertIn('<meta name="viewport" content="width=device-width, initial-scale=1.0">', self.html_content)

    def test_title_present(self):
        self.assertIn('<title>Hello World</title>', self.html_content)

if __name__ == '__main__':
    unittest.main()
