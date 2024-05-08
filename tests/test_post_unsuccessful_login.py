from tests.utils import load_json
import requests
from jsonschema import validate

def test_unsuccessful_login_user():
    url = "https://reqres.in/api"
    login = 'login'
    payload = {
        'email': 'peter@klaven'
    }

    response = requests.post(f'{url}/{login}', data=payload)

    assert response.status_code == 400
    validate(response.json(), load_json('post_unsuccessful_login.json'))
