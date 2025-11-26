import requests
import pytest
from dotenv import load_dotenv
import os


load_dotenv()

@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = requests.post(
        url="https://petstore.swagger.io/oauth/authorize",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
    assert response.status_code == 200