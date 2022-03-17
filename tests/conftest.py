import pytest
from app import app as f

@pytest.fixture()
def app():
    f.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield f # no sobrecarga memoria, se comparte la misma instancia en todos los tests

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()