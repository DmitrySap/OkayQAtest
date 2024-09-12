import requests
import json

class OkayQA:
    def __init__(self):
        self.base_url = 'https://okayqa-nest-api-cf2d5ab625fe.herokuapp.com/'
        self.my_token = self.get_token()[0]

    def get_token(self) -> json:
        data = {"email": "dmitriy.sapazhkou@okay.qa"}
        headers = {'Content-Type': 'application/json'}
        res = requests.post(self.base_url + 'auth/login', headers=headers, data=json.dumps(data))
        my_token = res.json().get("access_token")
        status = res.status_code
        print(my_token)
        print(status)
        return my_token, status

    def get_users(self) -> json:
        headers = {'Authorization': f'Bearer {self.my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        users = res.json()
        print(users) # для наглядности
        return status, users

