import requests

def test_not_found_user():
    url = "https://reqres.in/api"
    user_id = 23
    response = requests.get(f'{url}/users/{user_id}')

    assert response.status_code == 404
