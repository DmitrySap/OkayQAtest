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

def test_get_all_bugs():
    status, bugs = ok.get_all_bugs()
    assert status == 200
    assert len(bugs) > 0


def test_post_create_new_bug():
    title = "Баг"
    description = "Это тестовый баг"
    step = "Шаг чтобы воспроизвести баг"
    severity = "critical"
    priority = "high"
    fixed = False
    assignee = "Dmitriy"
    status, bug = ok.post_create_new_bug(title, description, step, severity, priority, fixed, assignee)
    assert status == 201
    assert bug['title'] == title, 'Неверный Title бага'
    assert bug['description'] == description, "Неверный Description бага"


def test_put_update_bug():
    bugs = ok.get_all_bugs()[1]
    last_bug_id = bugs[-1]['id']
    title = "Обновленный тайтл"
    description = "Обновленное описание"
    step = "Обновленный шаг"
    severity = "major"
    priority = "medium"
    fixed = True
    assignee = "Oleg"
    status, updated_bug = ok.put_update_bug(last_bug_id, title, description, step, severity, priority, fixed, assignee)
    assert status == 200
    assert updated_bug['title'] == title

