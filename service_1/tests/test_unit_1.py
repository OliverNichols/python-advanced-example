from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from service_1.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://service-2:5000/get/food', text='Margherita')
            m.get('http://service-3:5000/get/drink', text='Stella Artois')
            m.post('http://service-4:5000/post/order', json=16.78)

            response = self.client.get(url_for('index'))

        self.assert200(response)
        self.assertIn('You ordered a Margherita and a Stella Artois for £16.78.', response.data.decode())
        