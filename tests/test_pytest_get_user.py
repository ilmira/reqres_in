from typing import List

import pytest
import requests
from pydantic import BaseModel, HttpUrl


# Создайте функцию для получения данных пользователя по ID.
# Напишите тест, использующий эту функцию.
# Применните параметризацию для проверки нескольких ID пользователей.
# Используйте Pydantic для валидации ответа.

class UserItem(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class Support(BaseModel):
    url: HttpUrl
    text: str

class Meta(BaseModel):
    powered_by: str
    upgrade_url: HttpUrl
    docs_url: HttpUrl
    template_gallery: HttpUrl
    message: str
    features: List[str]
    upgrade_cta: str

class UserData(BaseModel):
    data: UserItem
    support: Support
    _meta: Meta

def get_user(user_id: int):
    return requests.get(f'https://reqres.in/api/users/{user_id}')


@pytest.mark.parametrize('user_id', [1, 2, 3])
def test_get_user(user_id):
    response = get_user(user_id)

    assert response.status_code == 200

    validated_user_data = UserData.model_validate(response.json())

    assert validated_user_data.data.id == user_id
