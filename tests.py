import unittest
from app import app

class TestHome(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.response = self.app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)
        
if __name__ == '__main__':
    unittest.main()