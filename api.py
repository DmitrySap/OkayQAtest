import requests
import json
from config import BASE_URL, EMAIL

class OkayQA:
    def __init__(self):
        self.base_url = BASE_URL
        self.my_token = self.get_token()[0]

    def get_token(self) -> json:
        data = EMAIL
        headers = {'Content-Type': 'application/json'}
        res = requests.post(self.base_url + 'auth/login', headers=headers, data=json.dumps(data))
        my_token = res.json().get("access_token")
        status = res.status_code
        print(my_token)
        print(status)
        return my_token, status

    def get_users(self) -> json:
        headers = {'Authorization': f'Bearer {self.my_token}', 'Content-Type': 'application/json'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        users = res.json()
        print(users)
        return status, users

    def get_all_bugs(self) -> json:
        headers = {'Authorization': f'Bearer {self.my_token}'}
        res = requests.get(self.base_url + 'bugs', headers=headers)
        status = res.status_code
        bugs = res.json()
        print(bugs)
        return status, bugs


    def post_create_new_bug(self, title, description, step, severity, priority, fixed, assignee) -> json:
        headers = {'Authorization': f'Bearer {self.my_token}', 'Content-Type': 'application/json'}
        data = {
            "title": title,
            "description": description,
            "str": [{"step": step}],
            "severity": severity,
            "prioriyt": priority,
            "fixed": fixed,
            "assignee": assignee
        }
        res = requests.post(self.base_url + 'bugs/create', headers=headers, data=json.dumps(data))
        status = res.status_code
        bug = res.json()
        print(bug)
        return status, bug

    def put_update_bug(self, last_bug_id, title, description, step, severity, priority, fixed, assignee) -> json:
        headers = {'Authorization': f'Bearer {self.my_token}', 'Content-Type': 'application/json'}
        data = {
            "title": title,
            "description": description,
            "str": [{"step": step}],
            "severity": severity,
            "prioriyt": priority,
            "fixed": fixed,
            "assignee": assignee
        }
        res = requests.put(self.base_url + f'bugs/{last_bug_id}', headers=headers, data=json.dumps(data))
        status = res.status_code
        updated_bug = res.json()
        print(updated_bug)
        return status, updated_bug
