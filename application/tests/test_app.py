from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import user, Product, orders

class TestBase(TestCase):                       
    def create_app(self):                       
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',   
            SECRET_KEY = "choochums",
            DEBUG = True,
            WTF_CSRF_ENABLED = False
                    )

        return app

