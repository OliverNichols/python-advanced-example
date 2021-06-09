from flask import url_for
from flask_testing import TestCase

from service_4.app import app, prices

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_food(self):

        for food in prices['food']:
            for drink in prices['drinks']:

                payload = {'food':food, 'drink':drink}
                response = self.client.post(url_for('post_order'), json=payload)

                self.assert200(response)

                expected_price = round((prices['food'][food] + prices['drinks'][drink]) * 1.1, 2)
                self.assertEqual(response.json, expected_price)
        