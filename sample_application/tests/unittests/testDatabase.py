import sys
import os
PROJECT_HOME = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(PROJECT_HOME)
import unittest
from flask.ext.testing import TestCase
import app
from models import db, Sample

class TestDatabase(TestCase):
    def create_app(self): 
        app_ = app.create_app()
        return app_
    def setUp(self): 
        db.create_all()
    def tearDown(self): 
        db.session.remove()
        db.drop_all()
    def test_something(self):
        '''Test if we can add/retrieve something from the database'''
        u = Sample(username='Foo Bar', password_hash='d90ea70cbf3115612b9755f435841026')
        db.session.add(u)
        db.session.commit()
        res = db.session.query(Sample).filter(Sample.username=='Foo Bar').first()
        self.assertEqual(res.username,'Foo Bar')
        self.assertEqual(res.password_hash,'d90ea70cbf3115612b9755f435841026')

if __name__ == '__main__':
    unittest.main(verbosity=2)
