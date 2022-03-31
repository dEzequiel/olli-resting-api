import pytest
from app import create_app


# The tests will look for fixture in the same file. As the fixture is not found in the file, it will check for fixture in conftest.py file.
# On finding it, the fixture method is invoked and the result is returned to the input argument of the test


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
