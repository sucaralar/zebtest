import pytest
from application import create_app, db as _db


@pytest.fixture(scope='session')
def app(request):
    app = create_app('testing')
    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()
    return app


@pytest.fixture(scope='session')
def db(app):
    _db.app = app
    _db.create_all()

    return _db



