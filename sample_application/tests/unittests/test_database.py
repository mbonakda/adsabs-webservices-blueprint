from flask.ext.testing import TestCase
from sample_application.app import create_app
from sample_application.models import db, FavoriteColor


class TestDatabase(TestCase):
    """
    Test flask-sqlalchemy database operations
    """
    def create_app(self):
        """
        Called once at the beginning of the tests; must return the application
        instance
        :return: flask.Flask application instance
        """
        _app = create_app()
        # Override whatever database uri is in the config for tests;
        # Use an in-memory sqlite database to ensure that no production data
        # are touched
        _app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"
        return _app

    def setUp(self):
        """
        setUp and tearDown are run at the start of each test; ensure
        that a fresh database is used for each test.
        """
        db.create_all()

    def tearDown(self):
        """
        setUp and tearDown are run at the start of each test; ensure
        that a fresh database is used for each test.
        """
        db.session.remove()
        db.drop_all()

    def test_add_entry(self):
        """
        Ensure that adding and retriving data from the database works
        """
        c = FavoriteColor(
            username='unittest',
            color='red'
        )
        db.session.add(c)
        db.session.commit()
        rv = FavoriteColor.query.filter_by(username='unittest').first()
        self.assertEqual(rv.username,'unittest')
        self.assertEqual(rv.color, 'red')