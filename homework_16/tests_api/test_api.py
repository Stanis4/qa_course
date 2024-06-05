from homework_16.backend import schemas
from homework_16.backend.pets_interface import pet_api
from homework_16.backend.schema_validation import validate_schema


def test_add_new_pet(generate_random_pet_id, clean_up_pet):
    payload = {
        "id": generate_random_pet_id,
        "category": {
            "id": 2,
            "name": "test"
        },
        "name": "bobby",
        "photoUrls": [
            "https://www.test.com"
        ],
        "tags": [
            {
                "id": 10,
                "name": "ten"
            }
        ],
        "status": "not available"
    }
    response = pet_api.create_pet(payload=payload)
    assert response.status_code == 200
    validate_schema(response.json(), schemas.ADD_PET)


def test_get_pet(create_pet, generate_random_pet_id):
    response = pet_api.find_pet_by_id(create_pet['id'])
    assert response.status_code == 200
    validate_schema(response.json(), schemas.ADD_PET)


def test_update_pet(create_pet, clean_up_pet):
    pet_id = create_pet['id']
    payload = {
        "id": pet_id,
        "category": {
            "id": 2,
            "name": "test"
        },
        "name": "Martie",
        "photoUrls": [
            "https://www.test.com"
        ],
        "tags": [
            {
                "id": 101,
                "name": "tens"
            }
        ],
        "status": "sold"
    }
    response = pet_api.update_pet(payload=payload)
    assert response.status_code == 200
    validate_schema(response.json(), schemas.ADD_PET)


def test_delete_pet(create_pet):
    response = pet_api.delete_pet(pet_id=create_pet['id'])
    assert response.status_code == 200
    validate_schema(response.json(), schemas.DELETE_PET)
