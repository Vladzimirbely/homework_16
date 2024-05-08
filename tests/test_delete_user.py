import requests

def test_delete():
    url = "https://reqres.in/api"
    user_id = 2
    response = requests.delete(f'{url}/users/{user_id}')

    assert response.status_code == 204
