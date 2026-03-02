import pytest

from clients.authentification.authentification_client import AuthentificationClient, get_authentification_client


@pytest.fixture
def authentification_client() -> AuthentificationClient:
    return get_authentification_client()