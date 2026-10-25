import unittest
from app import app
from recipes import RECIPES, compare

class WebsiteTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_and_assets(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        for name in ['style.css', 'app.js']:
            with self.client.get('/static/' + name) as response:
                self.assertEqual(response.status_code, 200)

    def test_empty_and_unknown(self):
        self.assertIn(b'Enter at least one', self.client.post('/', data={'ingredients': ' , '}).data)
        self.assertIn(b'No matches just yet', self.client.post('/', data={'ingredients': 'nonexistentzz'}).data)

    def test_every_recipe_unlocks_and_partial_instructions_stay_private(self):
        for name, recipe in RECIPES.items():
            with self.subTest(recipe=name):
                full = ', '.join(recipe['ingredients'])
                full_html = self.client.post('/', data={'ingredients': full}).get_data(as_text=True)
                # HTML escaping is expected; inspect the specific card.
                from markupsafe import escape
                card = full_html.split('<h3>' + str(escape(name)) + '</h3>', 1)[1].split('</article>', 1)[0]
                self.assertIn('Cooking instructions', card)
                for step in recipe['instructions']:
                    self.assertIn(str(escape(step)), card)
                partial_html = self.client.post('/', data={'ingredients': recipe['ingredients'][0]}).get_data(as_text=True)
                card = partial_html.split('<h3>' + str(escape(name)) + '</h3>', 1)[1].split('</article>', 1)[0]
                self.assertNotIn('Cooking instructions', card)
                for step in recipe['instructions']:
                    self.assertNotIn(str(escape(step)), card)

    def test_matching_and_sorting(self):
        self.assertEqual(compare([' TOMATOES ', 'EGGS', 'onions']), compare(['tomato', 'egg', 'onion']))
        matches = compare(['egg', 'butter', 'salt'])
        self.assertEqual([r['percentage'] for r in matches], sorted([r['percentage'] for r in matches], reverse=True))

    def test_escaped_input_and_limits(self):
        html = self.client.post('/', data={'ingredients':'<script>alert(1)</script>'}).data
        self.assertNotIn(b'<script>alert(1)</script>', html)
        self.assertIn(b'under 5,000', self.client.post('/', data={'ingredients':'x'*5001}).data)
        self.assertEqual(self.client.post('/', data={'ingredients':'x'*40000}).status_code, 413)

if __name__ == '__main__':
    unittest.main()
