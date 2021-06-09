from flask import url_for
from flask_testing import LiveServerTestCase
from urllib.request import urlopen
from selenium import webdriver
import re

from app import app # must be run from within container or module app won't be found here

food = ['Margherita', 'Vegetariana', 'Diavola']
drinks = ['Strongbow', 'Stella Artois', 'Prosecco']

class TestBase(LiveServerTestCase): 
    TEST_PORT=5500

    def create_app(self):
        app.config.update(
            LIVESERVER_PORT=self.TEST_PORT
        )
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=chrome_options)

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestResponse(TestBase):
    def test_index(self):

        for _ in range(20):
            self.driver.get(f'http://localhost:{self.TEST_PORT}')
            
            body = self.driver.find_element_by_tag_name('body')

            matches = re.findall(
                f"You ordered a ({'|'.join(food)}) and a ({'|'.join(drinks)}) for " + r"£(\d{2}\.\d{1,2})\.", 
                body.text
            )

            self.assertTrue(bool(matches)) # some results found matching regex
        