from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    # ensure the landing page get request responds with a 200 status code
    def test_landing_page_code(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # ensure that the landing page has the correct welcome message
    def test_landing_page_text(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b"Welcome to the API!" in response.data)
    
    # ensure that the landing page has the correct content type
    def test_landing_page_content_type(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
    
    # ensure that adding a pokemon adds it to the dictionary responds with a 201
    def test_adding_pokemon_post_code(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(name="Poliwhirl", level=28, in_party=False))
        self.assertEqual(response.status_code, 201)
    
    # ensure that adding a pokemon adds it to the dictionary responds with the correct content type
    def test_adding_pokemon_post_content_type(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(name="Poliwhirl", level=28, in_party=False))
        self.assertEqual(response.content_type, "application/json")
    
    # ensure that multiply by ten returns the correct value
    def test_multiply_ten_result(self):
        tester = app.test_client(self)
        response = tester.get('/multiply_ten/5', content_type='html/text')
        self.assertTrue(b'{"Result":50}' in response.data)


if __name__ == "__main__":
    unittest.main()