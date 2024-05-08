from tests.utils import load_json
import requests
from jsonschema import validate

def test_put_update():
    url = "https://reqres.in/api"
    user_id = 2

    payload = {
        "name": "name2",
        "job": "job2"
    }

    response = requests.put(f'{url}/users/{user_id}', data=payload)

    assert response.status_code == 200
    assert response.json()['name'] == 'name2'
    assert response.json()['job'] == 'job2'
    validate(response.json(), load_json('put_create_user.json'))
