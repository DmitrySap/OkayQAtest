import requests
from config import BASE_URL, EMAIL


def create_bug_data(title, description, step, severity, priority, fixed, assignee):
    return {
        "title": title,
        "description": description,
        "str": [{"step": step}],
        "severity": severity,
        "prioriyt": priority,
        "fixed": fixed,
        "assignee": assignee
    }


class OkayQA:
    def __init__(self):
        self.base_url = BASE_URL
        self.my_token = self.get_token()[1]

    def request(self, method: str, endpoint: str, json_data=None):
        headers = {'Authorization': f'Bearer {self.my_token}', 'Content-Type': 'application/json'}
        response = requests.request(method, f'{self.base_url}{endpoint}', headers=headers, json=json_data)
        return response.status_code, response.json()

    def get_token(self):
        response = requests.post(f'{self.base_url}auth/login',
                                 headers={'Content-Type': 'application/json'},
                                 json=EMAIL)
        return response.status_code, response.json().get("access_token")

    def get_users(self):
        return self.request('GET', 'users')

    def get_all_bugs(self):
        return self.request('GET', 'bugs')

    def post_create_new_bug(self, title, description, step, severity, priority, fixed, assignee):
        bug_data = create_bug_data(title, description, step, severity, priority, fixed, assignee)
        return self.request('POST', 'bugs/create', bug_data)

    def put_update_bug(self, last_bug_id, title, description, step, severity, priority, fixed, assignee):
        bug_data = create_bug_data(title, description, step, severity, priority, fixed, assignee)
        return self.request('PUT', f'bugs/{last_bug_id}', bug_data)
