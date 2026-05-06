import allure

from services.base_api import BaseAPI
from services.reqres_in.users.models.users import UserData


class GetUser(BaseAPI):

    def __init__(self, env_config):
        """
        Args:
            env_config (EnvironmentConfig): Конфигурация окружения из фикстуры
        """
        super().__init__(base_url=env_config.reqres_url)

    @allure.step('Просмотр данных пользователя по id')
    def get_user(self, id: int):

        response = self.session.get(f"{self.base_url}/users/{id}")
        return response

    def check_user_data(self, response, id: int, valid=True):
        if valid:
            with allure.step('Проверка данных по id: проверка наличия id'):
                assert response.json()['data']['id']
            with allure.step(f'Проверка данных по id: проверка id: ожидается {id}'):
                assert response.json()['data']['id'] == id
        else:
            with allure.step('Невалидная проверка'):
                assert not response.json()

    def validate_data(self, response, user_id):
        with allure.step('Валидация ответа по Pydantic-схеме UserData'):
            validated_user_data = UserData.model_validate(response.json())
        with allure.step(f'Проверка id, ожидается {user_id}'):
            assert validated_user_data.data.id == user_id
