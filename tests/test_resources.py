import allure
import pytest

from services.reqres_in.resources.get_resource import GetResource
from services.reqres_in.resources.get_resources import GetResources
from services.reqres_in.resources.models.resource import ResourcesListResponse, SingleResourceResponse
from utils.helper import Helper


@allure.feature('Resources')
class TestResources:
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Получить список ресурсов')
    @allure.testcase("https://example.com/testcase/8", "Test-8")
    def test_get_resources(self, app):
        response = app.get_resources.get_resources()
        app.get_resources.check_status_code_is_200(response)
        app.get_resources.validate_data(response)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Получить ресурс')
    @allure.testcase("https://example.com/testcase/9", "Test-9")
    def test_get_resource(self, app):
        id = 2
        response = app.get_resource.get_resource(id)

        app.get_resource.check_status_code_is_200(response)
        app.get_resource.validate_data(response)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title('Получить несуществующий ресурса')
    @allure.testcase("https://example.com/testcase/10", "Test-10")
    def test_get_wrong_resource(self, app):
        id = 23
        response = app.get_resource.get_resource(id)
        app.get_resource.check_status_code_is_404(response)
