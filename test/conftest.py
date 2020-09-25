import pytest

from server import create_app
from server.util.instances import db
from server.models.User import User

@pytest.fixture
def app():
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        user = User(
            email='ebube@cortts.com',
            password='pbkdf2:sha256:150000$eGO8fIQ6$8c390d52bd557b4e3a4e1521efe103be9a5cb9cb4db3d0d2dfe3cc29e40ecd41',
            phone='08162300796',
            name='Ebubechukwu',
            username="Ebube12"
        )
    
        db.session.add(user)
        db.session.commit()
    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    return app.test_cli_runner()