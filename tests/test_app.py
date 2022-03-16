# from flask_testing import TestCase
# from selenium import webdriver
# from urllib.request import urlopen
# from flask import url_for

# from application import app, db
# from application.models import user, Product, orders
# from application.forms import AddProduct, AddUser, AddCart

# class TestBase(TestCase):
#     def create_app(self):
#         app.config.update(
#             SQLALCHAMEY_DATABASE_URI = 'sqlite:///test.db',
#             SECRET_KEY = "choochums",
#             LIVESERVER_PORT = 5000,
#             DEBUG = True,
#             TESTING = True,
#             WTF_CSRF_ENABLED = False
#         )
#         return app

#     def setUp(self):
#         chrome_options = webdriver.chrome.options.Options()
#         chrome_options.add_argument('--headless')
#         self.driver = webdriver.Chrome(options = chrome_options)
#         db.create_all()
#         self.driver.get(f'http://localhost:5000/add_user')
#         db.create_all()
#         test_product = product('Meow', 15.00, 'Meow Treat', 10)('Sleepies', 18.00, 'Dreamies Improved', 10)
#         test_user = ('Bilal', 'ellahiphotography@gmail.com', '5 Robinson Close, Leytonstone, London'), ('Adam', 'Adamisawesome@qa.co.uk', '69 QA Street, London, 433 7AB')
#         db.session.add(test_product)
#         db.session.add(test_user)
#         db.session.commit()

#     def tearDown(self):
#         self.driver.quit()
#         db.drop_all()
    
#     def test_server_running(self):
#         response = urlopen('http://localhost:5000/add_user')
#         self.assertEqual(response.code, 200)

   
#     def test_add_user(self):
#         for i in self.TEST_CASES:
#             self.submit_input(i)
#             users = user.query.filter_by(username=case[0]).all()
#             self.assertNotEqual(users, None)

# def test_add_product(self):
#         for i in self.TEST_CASES:
#             self.submit_input(i)
#             products = user.query.filter_by(product_name=case[0]).all()
#             self.assertNotEqual(user, None)
    
# def submit_input(self, case):
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/select[1]').click()
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/select[2]').click()
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[3]').send_keys(case[2])
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[3]').send_keys(case[3])
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/form/input[4]').send_keys(case[4])
#         self.driver.find_element_by_xpath('//*[@id="submit"]').click()

# class TestUpdateQuantity(TestBase):
#     def test_updatequantity_get(self):
#         response = self.client.get(url_for('update_quantity', pk = 1))
#         self.assert200(response)
#         self.assertIn(b'Quantity', response.data)

#     def test_updatequantity_post(self):
#         response = self.client.post(
#         url_for('update_quantity', pk = 1),
#         data = dict(quantity = "Updated quantity", quantity_desc = "updated quantity for testing"))
#         self.assert200(response)
#         self.assertIn(b'quantity has been updated successfully!', response.data)
#         self.assertNotEqual(quantity.query.filter_by(quantity = "Updated quantity").first(), None)


# class TestDeleteItem(TestBase):
#     def test_deleteitem_get(self):
#         response = self.client.get(url_for('delete_item', pk = 2))
#         self.assert200(response)
#         self.assertIn(b'Item has been deleted successfully!', response.data)
#         self.assertEqual(item.query.filter_by(item_name = 'Test item').first(),None)




from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import user, Product, orders
from application.forms import AddProduct, AddUser, AddCart


class TestBase(TestCase):
    def create_app(self): #sets test configuration
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = "choochums",
            LIVESERVER_PORT = 5000,
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self): #run before each test
        db.create_all()
        test_product = Product(product_name='Sample Product', product_description ='Sample desc', product_cost =1, product_quantity=1)
        test_product_2 = Product(product_name='Sample Product 2', product_description ='Sample desc', product_cost =1, product_quantity=1)
        test_user = user(username='Sample Name', email ='sample@gmail.com', address = 'Sample Address')

        db.session.add(test_product)
        db.session.add(test_user)
        db.session.commit()


    def tearDown(self): #run after each test
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)
        self.assertIn(b'Home', response.data)

    def test_home_shoppingcart(self):
        response = self.client.get(url_for('Shopping_Cart'))
        self.assert200(response)
        self.assertIn(b'Shopping Cart', response.data)
    
    def test_home_product(self):
        response = self.client.get(url_for('add_an_item'))
        self.assert200(response)
        self.assertIn(b'Add an item', response.data)
    
    def test_home_user(self):
        response = self.client.get(url_for('add_user'))
        self.assert200(response)
        self.assertIn(b'Add an user', response.data)


class TestAddItem(TestBase):
    def test_item_get(self):
        response = self.client.get(url_for('add_an_item'))
        self.assert200(response)
        self.assertIn(b'product_name', response.data)

    def test_item_post(self):
        response = self.client.post(
            url_for('add_an_item'),
            data = dict(product_name='Sample Product', product_description ='Sample desc', product_cost =1, product_quantity=1),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'product_name', response.data)

class TestAddUser(TestBase):
    def test_user_get(self):
        response = self.client.get(url_for('add_user'))
        self.assert200(response)
        self.assertIn(b'username', response.data)

    def test_create_user(self):
        response = self.client.post(
            url_for('add_user'),
            data = dict(username='username', email ='sample@gmail.com', address = 'Sample Address'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'username', response.data)



class TestViewAllProducts(TestBase): # test for viewing all items
    def test_view_products_get(self):
        response = self.client.get(url_for('add_an_item'))
        self.assert200(response)
        self.assertIn(b'Sample Product', response.data)

class TestUpdateQuantity(TestBase): # test for updating quantity of items
    def test_update_quantity_get(self):
        response = self.client.get(url_for('add_an_item'))
        self.assert200(response)
        self.assertIn(b'product_quantity', response.data)

    def test_update_quantity_post(self):
        response = self.client.post(
        url_for('add_an_item'),
        data = dict(product_name='Sample item', product_cost=56.00,product_description= 'Sample desc', product_quantity=20))
        self.assert200(response)
        self.assertNotEqual(Product.query.filter_by(product_quantity = 20).first(), None)


class TestDeleteProduct(TestBase): # testing for deleting an item
    def test_delete_product_get(self):
        response = self.client.get(url_for('add_an_item'))
        self.assert200(response)
        self.assertEqual(Product.query.filter_by(product_name = 'Sample item 2').first(),None)