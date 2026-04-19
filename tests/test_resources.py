import allure
import pytest

from services.reqres_in.resources.get_resource import GetResource
from services.reqres_in.resources.get_resources import GetResources
from services.reqres_in.resources.models.resource import ResourcesListResponse, SingleResourceResponse
from utils.helper import Helper


@allure.feature('Resources')
class TestResources:
    helper = Helper()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Получить список ресурсов')
    @allure.testcase("https://example.com/testcase/8", "Test-8")
    def test_get_resources(self, env_config):
        with allure.step('Получаем список ресурсов'):
            response = GetResources(env_config).get_resources()
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = ResourcesListResponse.model_validate(response.json())
            assert len(validated_data.data) == validated_data.per_page

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Получить ресурс')
    @allure.testcase("https://example.com/testcase/9", "Test-9")
    def test_get_resource(self, env_config):
        id = 2
        with allure.step('Получаем ресурс'):
            response = GetResource(env_config).get_resource(id)
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 200
        with allure.step('Валидация схемы ответа'):
            validated_data = SingleResourceResponse.model_validate(response.json())

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Получить несуществующий ресурса')
    @allure.testcase("https://example.com/testcase/10", "Test-10")
    def test_get_wrong_resource(self, env_config):
        id = 23
        with allure.step('Пытаемся получить ресурс'):
            response = GetResource(env_config).get_resource(id)
            self.helper.attach_response(response.json())

        with allure.step('Проверяем статус код'):
            assert response.status_code == 404
