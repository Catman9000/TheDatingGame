from flask_testing import LiveServerTestCase 
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import user, Product, orders
from application.forms import AddProduct, AddUser, AddCart

class TestBase(LiveServerTestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            LIVESERVER_PORT = 5050,
            DEBUG = True,
            TESTING = True
        )
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options = chrome_options)
        db.create_all()
        self.driver.get(f'http://localhost:{self.TEST_PORT}/add_an_item')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()

    # def test_server_running(self):
    #     response = urlopen(f'http://localhost:5050/add_an_item')
    #     self.assert200(response)

class TestAddProject(TestBase):
    TEST_CASES = ('Sample Product', 'Sample desc', 1, 1), ('Sample Product 2', 'Sample desc 2', 2, 2)

    def submit_input(self, case):
        self.driver.find_element_by_xpath ('/html/body/form/input[1]').send_keys()(case[0])
        self.driver.find_element_by_xpath ('/html/body/form/input[2]').send_keys()(case[0])
        self.driver.find_element_by_xpath ('/html/body/form/input[3]').send_keys()(case[0])
        self.driver.find_element_by_xpath ('/html/body/form/input[4]').send_keys()(case[0])
        self.driver.find_element_by_xpath ('/html/body/form/input[5]').click()

    def test_add_an_item(self):
        for case in self.TEST_CASES:
            self.submit_input(case)
            products = Product.query.filter_by(product_name=case[0])
            self.assertBitEqual(products, None)
            

        
