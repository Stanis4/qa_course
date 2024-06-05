import random
from http.client import HTTPException

import pytest

from homework_16.backend.pets_interface import pet_api


@pytest.fixture()
def generate_random_pet_id():
    return random.randint(0, 999)


@pytest.fixture()
def create_pet(generate_random_pet_id):
    payload = {
        "id": generate_random_pet_id,
        "category": {
            "id": 2,
            "name": "test"
        },
        "name": "bobby",
        "photoUrls": [
            "https://www.foof.com"
        ],
        "tags": [
            {
                "id": 10,
                "name": "ten"
            }
        ],
        "status": "fake"
    }
    response = pet_api.create_pet(payload=payload)
    return response.json()


@pytest.fixture
def clean_up_pet(generate_random_pet_id):
    yield
    response = pet_api.delete_pet(pet_id=generate_random_pet_id)
    if response.status_code != 200:
        raise HTTPException(response.text)







