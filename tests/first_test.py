import requests
from utilities.test_base import TestBase


class TestLogin(TestBase):

    def get_token(self, url, expected_status_code):
        headers = {
            'Accept': "application/json"
        }
        response = requests.request("GET", url, headers=headers)
        assert response.status_code == expected_status_code
        assert response.json() is not None
        assert response.json()['Token'] is not None
        assert response.json()['items'] is not None

    def test_success_get_token(self):
        url = self.base_url + self.test_data['login_url']
        self.get_token(url, 200)
