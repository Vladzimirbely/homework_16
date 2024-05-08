from tests.utils import load_json
import requests
from jsonschema import validate

def test_post_create():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "name",
        "job": "job"
    }

    response = requests.post(url, data=payload)

    assert response.status_code == 201
    assert response.json()['name'] == 'name'
    assert response.json()['job'] == 'job'
    validate(response.json(), load_json('post_create_user.json'))
