from api import OkayQA

ok = OkayQA()

def test_get_token():
    result = ok.get_token()
    token = result[0]
    status = result[1]
    assert status == 201
    assert token is not None

def test_get_users():
    status, users = ok.get_users()
    assert status == 200
    assert len(users) > 0
    user_found = next(user for user in users if user['name'] == "Igor Okay")
    assert user_found['role'] == "admin"
