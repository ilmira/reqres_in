import os

import allure
import pytest


@allure.feature('Users')
class TestUser:
    @pytest.mark.skipif("SKIP_TEST" in os.environ, reason="Переменная окружения SKIP_TEST установлена")
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Обновление данных пользователя PUT')
    @allure.testcase("https://example.com/testcase/5", "Test-5")
    def test_update_user_put(self, app):
        id = 2
        with allure.step('Обновляем данные пользователя'):
            response = app.update_put.update_user_put(id, name="John Doe UPD", job="QA Engineer UPD")

        app.update_put.check_status_code_is_200(response)
        app.update_put.validate_data(response)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Обновление данных пользователя PATCH')
    @allure.testcase("https://example.com/testcase/6", "Test-6")
    def test_update_user_patch(self, app):
        id = 2
        response = app.update_patch.update_user_patch(id, name="John Doe UPD", job="QA Engineer UPD")
        app.update_patch.check_status_code_is_200(response)
        app.update_patch.validate_data(response)

    @pytest.mark.regression
    @allure.title('Удаление пользователя')
    @allure.testcase("https://example.com/testcase/7", "Test-7")
    def test_delete_user(self, app):
        id = 2
        response = app.delete.delete_user(id)

        app.delete.check_status_code_is_204(response)

        app.delete.check_delete(id)
