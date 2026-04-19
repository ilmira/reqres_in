# conftest.py
import pytest
from faker import Faker

from config.environments import Environment, environments, EnvironmentConfig
from services.reqres_in.users.delete_user import DeleteUser
from services.reqres_in.users.create_user import CreateUser


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
