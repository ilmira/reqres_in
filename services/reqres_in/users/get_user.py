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

    @allure.step('Проверка данных по id')
    def check_user_data(self, response, valid = True):
        if valid:
            assert response.json()['data']['id']
            assert response.json()['data']['id'] == 2
        else:
            assert not response.json()

    @allure.step('Валидация схемы ответа')
    def validate_data(self, response, user_id):
        validated_user_data = UserData.model_validate(response.json())
        assert validated_user_data.data.id == user_id


