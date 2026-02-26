import pytest

from clients.authentification.authentification_client import AuthentificationClient, get_authentification_client
from clients.users.public_users_cliens import get_public_users_client, PublicUserClient


@pytest.fixture
def authentification_client() -> AuthentificationClient:
    return get_authentification_client()

@pytest.fixture
def public_users_client() -> PublicUserClient:
    return get_public_users_client()