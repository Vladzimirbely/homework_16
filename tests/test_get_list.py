from tests.utils import load_json
import requests
from jsonschema import validate

def test_get_list_users():
    url = "https://reqres.in/api/"
    page_id = 2
    response = requests.get(f'{url}users?page={page_id}')

    assert response.status_code == 200
    assert response.json()['total'] == 12
    assert response.json()['total_pages'] == 2
    validate(response.json(), load_json('get_list_users.json'))
