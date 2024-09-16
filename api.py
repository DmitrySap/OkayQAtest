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

def create_testcase_data(title, precondition, steps, expected, owner, active):
    return {
        "title": title,
        "precondition": precondition,
        "steps": [steps],
        "expected": expected,
        "owner": owner,
        "active": active,
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

    def delete_user(self, user_id):
        return self.request('DELETE', f'users/{user_id}')

    def create_new_testcase(self, title, precondition, steps, expected, owner, active):
        testcase_data = create_testcase_data(title, precondition, steps, expected, owner, active)
        return self.request("POST", 'test-cases/create', testcase_data)

    def get_all_testcases(self):
        return self.request('GET', 'test-cases')

    def delete_testcases(self, testcase_id):
        return self.request('DELETE', f'test-cases/{testcase_id}')