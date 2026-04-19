import pytest
import requests
from faker import Faker

from services.reqres_in.users.models.users import CreateUserResponse

fake = Faker()


@pytest.fixture
def user_data():
    return {
        "name": fake.name(),
        "job": fake.job()
    }


def create_user(user_data: dict):
    return requests.post('https://reqres.in/api/users', json=user_data, headers={'x-api-key': 'reqres-free-v1'})


def test_create_user(user_data):
    response = create_user(user_data)

    assert response.status_code == 201

    validated_data = CreateUserResponse.model_validate(response.json())

    assert validated_data.id
    assert validated_data.name == user_data['name']
    assert validated_data.job == user_data['job']
