"""Модуль с автотестами"""
from faker import Faker
from api import OkayQA

fake = Faker()
ok = OkayQA()

def test_get_token():
    """Проверка успешности получения токена"""
    status, token= ok.get_token()
    assert status == 201
    assert token is not None

def test_get_users():
    """Проверка успешности получения списка пользователей"""
    status, users = ok.get_users()
    assert status == 200
    assert len(users) > 0
    user_found = next(user for user in users if user['name'] == "Igor Okay")
    assert user_found['role'] == "admin"

def test_get_all_bugs():
    """Проверка успешности получения всех багов"""
    status, bugs = ok.get_all_bugs()
    assert status == 200
    assert len(bugs) > 0

def test_post_create_new_bug():
    """Проверка успешности создания бага"""
    title = "Баг"
    description = "Это тестовый баг"
    step = "Шаг чтобы воспроизвести баг"
    severity = "critical"
    priority = "high"
    fixed = False
    assignee = "Dmitriy"

    status, bug = ok.post_create_new_bug(title, description, step,
                                         severity, priority, fixed, assignee)
    assert status == 201
    assert bug['title'] == title, 'Неверный Title бага'
    assert bug['description'] == description, "Неверный Description бага"

def test_put_update_bug():
    """Проверка успешности обновления бага"""
    bugs = ok.get_all_bugs()[1]
    last_bug_id = bugs[-1]['id']
    title = fake.sentence(nb_words=3)
    description = fake.sentence()
    step = fake.sentence()
    severity = "major"
    priority = "medium"
    fixed = fake.boolean()
    assignee = fake.name()

    status, updated_bug = ok.put_update_bug(last_bug_id, title, description, step,
                                            severity, priority, fixed, assignee)
    assert status == 200
    assert updated_bug['title'] == title
    assert updated_bug['description'] == description, "Неверный Description бага"


def test_delete_user():
    """Проверка успешности удаления пользователя"""
    user_id = 1
    status, response = ok.delete_user(user_id)
    assert status == 403, "Ожидаемый статус 403 Forbidden"
    assert response['message'] == "Insufficient role", "Ожидаемое сообщение 'Insufficient role'"
    assert response['error'] == "Forbidden", "Ожидаемая ошибка 'Forbidden'"

def test_create_testcase():
    """Проверка успешности создания тесткейса"""
    title = fake.sentence(nb_words=3)
    precondition = fake.sentence()
    steps = fake.sentence()
    expected = fake.sentence()
    owner = fake.name()
    active = fake.boolean()

    status, testcase = ok.create_new_testcase(title, precondition, steps, expected, owner, active)
    assert status == 201
    assert testcase['title'] == title, 'Неверный Title тесткейса'
    assert testcase['precondition'] == precondition, "Неверный Precondition тесткейса"

def test_get_all_testcases():
    """Проверка успешности получения всех тесткейсов"""
    status, testcases = ok.get_all_testcases()
    assert status == 200
    assert len(testcases['data']) > 0, "Не найдено тесткейсов"

def test_delete_all_testcases():
    """Проверка успешности удаления всех тесткейсов"""
    status, testcases = ok.get_all_testcases()
    assert status == 200, "Ошибка получения тесткейсов"
    assert len(testcases['data']) > 0, "Не найдено тесткейсов для удаления"

    for testcase in testcases['data']:
        testcase_id = testcase['id']
        delete_status = ok.delete_testcases(testcase_id)
        assert delete_status == 200, f"Ошибка при удалении тесткейса с ID {testcase_id}"
