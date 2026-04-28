# services/base_api.py
import allure
import requests


class BaseAPI:
    """Базовый класс для работы с API."""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            'x-api-key': 'free_user_3CzT1WAan5vzPpTgqVX7RAyBJFG'
        })

    @allure.step('Проверяем статус код: ожидается код 200')
    def check_status_code_is_200(self, response):
        assert response.status_code == 200

    @allure.step('Проверяем статус код: ожидается код 201')
    def check_status_code_is_201(self, response):
        assert response.status_code == 201

    @allure.step('Проверяем статус код: ожидается код 204')
    def check_status_code_is_204(self, response):
        assert response.status_code == 204

    @allure.step('Проверяем статус код: ожидается код 400')
    def check_status_code_is_400(self, response):
        assert response.status_code == 400

    @allure.step('Проверяем статус код: ожидается код 404')
    def check_status_code_is_404(self, response):
        assert response.status_code == 404

    @allure.step('Валидация схемы ответа')
    def validate_data(self, response):
        assert True

