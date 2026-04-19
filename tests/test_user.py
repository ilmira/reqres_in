import os

import allure
import pytest

from services.reqres_in.users.create_user import CreateUser
from services.reqres_in.users.delete_user import DeleteUser
from services.reqres_in.users.get_user import GetUser
from services.reqres_in.users.get_users import GetUsers
from services.reqres_in.users.models.users import CreateUserResponse, SingleUserResponse, UpdateUserResponse, \
    UsersListResponse
from services.reqres_in.users.update_user_patch import UpdateUserPatch
from services.reqres_in.users.update_user_put import UpdateUserPut
from utils.helper import Helper


@pytest.fixture
def user_data():
    return {}


@pytest.fixture
def delete_user(env_config, user_data):
    """
    Фикстура для удаления тестового пользователя.
    Выполняется только в тестах, где явно указана.
    """
    yield

    if "id" in user_data:
        with allure.step('Удаляем тестового пользователя'):
            response = DeleteUser(env_config).delete(user_data["id"])
            assert response.status_code == 204


@allure.feature('Users')
class TestUser:
    helper = Helper()

    @pytest.mark.skipif("SKIP_TEST" in os.environ, reason="Переменная окружения SKIP_TEST установлена")
    @pytest.mark.regression
    @allure.title('Создание нового пользователя')
    @allure.testcase("https://example.com/testcase/1", "Test-1")
    def test_create_user(self, env_config, delete_user):
        with allure.step('Создаем нового пользователя'):
            response = CreateUser(env_config).create_user(
                name="John Doe",
                job="QA Engineer"
            )
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 201

        with allure.step('Валидация схемы ответа'):
            validated_data = CreateUserResponse.model_validate(response.json())
            assert validated_data.name == "John Doe"
            assert validated_data.job == "QA Engineer"

    @pytest.mark.get_users
    @pytest.mark.smoke
    @allure.title('Получить список пользователей')
    @allure.testcase("https://example.com/testcase/2", "Test-2")
    def test_get_users(self, env_config):
        page_number = 2
        with allure.step('Получаем список пользователей'):
            response = GetUsers(env_config).get_users(page_number)
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = UsersListResponse.model_validate(response.json())
            assert validated_data.page == page_number
            assert len(validated_data.data) != 0

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Получить данные пользователя')
    @allure.testcase("https://example.com/testcase/3", "Test-3")
    def test_get_user(self, env_config):
        id = 2
        with allure.step('Получаем данные пользователя'):
            response = GetUser(env_config).get_user(id)
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = SingleUserResponse.model_validate(response.json())
            print(validated_data)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Получить данные несуществующего пользователя')
    @allure.testcase("https://example.com/testcase/4", "Test-4")
    def test_get_wrong_user(self, env_config):
        id = 23
        with allure.step('Пытаемся получить данные пользователя'):
            response = GetUser(env_config).get_user(id)
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 404

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Обновление данных пользователя PUT')
    @allure.testcase("https://example.com/testcase/5", "Test-5")
    def test_update_user_put(self, env_config):
        id = 2
        with allure.step('Обновляем данные пользователя'):
            response = UpdateUserPut(env_config).update_user_put(id, name="John Doe UPD", job="QA Engineer UPD")
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = UpdateUserResponse.model_validate(response.json())

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Обновление данных пользователя PATCH')
    @allure.testcase("https://example.com/testcase/6", "Test-6")
    def test_update_user_patch(self, env_config):
        id = 2
        with allure.step('Обновляем данные пользователя'):
            response = UpdateUserPatch(env_config).update_user_patch(id, name="John Doe UPD", job="QA Engineer UPD")
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = UpdateUserResponse.model_validate(response.json())

    @pytest.mark.regression
    @allure.title('Удаление пользователя')
    @allure.testcase("https://example.com/testcase/7", "Test-7")
    def test_delete_user(self, env_config):
        id = 2
        with allure.step('Удаляем пользователя'):
            response = DeleteUser(env_config).delete_user(id)
            self.helper.attach_response(response.text)

        with allure.step('Проверяем статус код'):
            assert response.status_code == 204

        with allure.step('Проверяем тело ответа'):
            assert response.text == ''
