from app import app
import unittest
import json

class FlaskTestCase(unittest.TestCase):
    def test_modify_map(self):
        with app.test_client() as c:
            rv = c.put('/maps/bellevue', json={
                "buildings": {
                    "a": { "b": 1 },
                    "b": { "a": 2 },
                    "c": { "d": 3 },
                    "d": { "c": 4 }
                }
            })
            json_data = rv.get_json()
            json_data = json.dumps(json_data, sort_keys=True)
            expected_data = json.dumps({
                'buildings': {
                    "a": { "b": 1 },
                    "b": { "a": 2 },
                    "c": { "d": 3 },
                    "d": { "c": 4 }
                }}, sort_keys=True)
            assert json_data == expected_data

    # ensure the landing page get request responds with a 200 status code
    def test_find_shortest_route(self):
        tester = app.test_client(self)
        response = tester.get('/maps/bellevue/path/A/B', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.body, json.dumps({"distance": 0, "path": []}))
    
    # # ensure that the landing page has the correct welcome message
    # def test_landing_page_text(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/', content_type='html/text')
    #     self.assertTrue(b"Welcome to the API!" in response.data)
    
    # # ensure that the landing page has the correct content type
    # def test_landing_page_content_type(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/', content_type='html/text')
    #     self.assertEqual(response.content_type, "text/html; charset=utf-8")
    
    # # ensure that adding a pokemon adds it to the dictionary responds with a 201
    # def test_adding_pokemon_post_code(self):
    #     tester = app.test_client(self)
    #     response = tester.post('/', data=dict(name="Poliwhirl", level=28, in_party=False))
    #     self.assertEqual(response.status_code, 201)
    
    # # ensure that adding a pokemon adds it to the dictionary responds with the correct content type
    # def test_adding_pokemon_post_content_type(self):
    #     tester = app.test_client(self)
    #     response = tester.post('/', data=dict(name="Poliwhirl", level=28, in_party=False))
    #     self.assertEqual(response.content_type, "application/json")
    
    # # ensure that multiply by ten returns the correct value
    # def test_multiply_ten_result(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/multiply_ten/5', content_type='html/text')
    #     self.assertTrue(b'{"Result":50}' in response.data)


if __name__ == "__main__":
    unittest.main()