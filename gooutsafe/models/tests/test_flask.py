import pytest

from gooutsafe import create_app


@pytest.fixture
def client():
    create_app('config.TestConfig')

