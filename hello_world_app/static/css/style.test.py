
import unittest
import os

class TestStyleCss(unittest.TestCase):

    def setUp(self):
        self.css_path = os.path.join(os.path.dirname(__file__), 'style.css')
        with open(self.css_path, 'r') as f:
            self.css_content = f.read()

    def test_body_centering_rules(self):
        self.assertIn('body {', self.css_content)
        self.assertIn('display: flex;', self.css_content)
        self.assertIn('justify-content: center;', self.css_content)
        self.assertIn('align-items: center;', self.css_content)
        self.assertIn('min-height: 100vh;', self.css_content)
        self.assertIn('margin: 0;', self.css_content)

    def test_h1_styling_rules(self):
        self.assertIn('h1 {', self.css_content)
        self.assertIn('color: #333;', self.css_content)
        self.assertIn('font-size: 3em;', self.css_content)
        self.assertIn('text-align: center;', self.css_content)
        self.assertIn('font-family: Arial, sans-serif;', self.css_content)

if __name__ == '__main__':
    unittest.main()
