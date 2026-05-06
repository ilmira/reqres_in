import os

import allure
import requests
from dotenv import load_dotenv

load_dotenv()


class BaseAPI:
    """Базовый класс для работы с API."""

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.api_key = os.getenv('API_KEY')
        if not self.api_key:
            raise ValueError("API_KEY environment variable is not set")
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            'x-api-key': self.api_key
        })

    def check_status_code_is_200(self, response):
        with allure.step('Проверяем статус код: ожидается код 200'):
            assert response.status_code == 200

    def check_status_code_is_201(self, response):
        with allure.step('Проверяем статус код: ожидается код 201'):
            assert response.status_code == 201

    def check_status_code_is_204(self, response):
        with allure.step('Проверяем статус код: ожидается код 204'):
            assert response.status_code == 204

    def check_status_code_is_400(self, response):
        with allure.step('Проверяем статус код: ожидается код 400'):
            assert response.status_code == 400

    def check_status_code_is_404(self, response):
        with allure.step('Проверяем статус код: ожидается код 404'):
            assert response.status_code == 404

    def validate_data(self, **args):
        with allure.step('Валидация ответа по Pydantic-схеме'):
            raise NotImplementedError
