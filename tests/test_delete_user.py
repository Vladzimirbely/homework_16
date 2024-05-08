import requests
from jsonschema import validate

from tests.utils import load_json


def test_delete():
    url = "https://reqres.in/api"
    user_id = 2
    response = requests.delete(f'{url}/users/{user_id}')

    assert response.status_code == 204
