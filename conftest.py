import pytest
from faker import Faker

from config.application import Application
from config.environments import Environment, environments, EnvironmentConfig
from services.base_api import BaseAPI
from services.reqres_in.auth.login_user import LoginUser
from services.reqres_in.auth.models.auth import RegisterRequest
from services.reqres_in.auth.register_user import RegisterUser
from services.reqres_in.resources.get_resources import GetResources
from services.reqres_in.users.delete_user import DeleteUser
from services.reqres_in.users.create_user import CreateUser
from services.reqres_in.users.get_user import GetUser


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="stage",
        help="Окружение для запуска тестов (dev/stage)"
    )


@pytest.fixture(scope="session")
def env(request) -> Environment:
    """Фикстура для получения текущего окружения"""
    env_name = request.config.getoption("--env")
    try:
        return Environment(env_name.lower())
    except ValueError:
        raise ValueError(
            f"Некорректное окружение: {env_name}. "
            f"Используйте одно из: dev/stage/prod"
        )


@pytest.fixture(scope="session")
def env_config(env) -> EnvironmentConfig:
    """Фикстура для получения конфигурации текущего окружения"""
    print(f"\nОкружение: {env}")
    print(f"{environments[env]}\n")
    return environments[env]

fake = Faker()

@pytest.fixture
def user_data():
    return {
        "name": fake.name(),
        "job": fake.job()
    }

@pytest.fixture(scope='session')
def new_user_id(env_config, user_data):
    user_id = CreateUser(env_config).create_user(user_data['name'], user_data['job']).json()['id']
    yield user_id
    DeleteUser(env_config).delete_user(user_id)

@pytest.fixture(scope='session')
def user_factory(env_config):
    created_ids = []

    def _create_user(name, job):
        user_response = CreateUser(env_config).create_user(name, job)
        created_ids.append(user_response.json()['id'])
        return user_response

    yield _create_user

    for user_id in created_ids:
        DeleteUser(env_config).delete_user(user_id)


@pytest.fixture(scope='session')
def app(env_config):
    return Application(env_config)


@pytest.fixture(scope='session')
def register_data_valid():
    return RegisterRequest(email='eve.holt@reqres.in', password='pistol')
