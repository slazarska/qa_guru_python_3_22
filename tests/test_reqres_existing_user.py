from pytest_voluptuous import S
from requests import Response

import schemas.reqres_user_schemas


new_data_user_payload = {
    "name": "Newton Scamander",
    "job": "Author"
}


def test_update_existing_user(reqres):
    response: Response = reqres.put(url='/api/users/2', data=new_data_user_payload)

    assert response.status_code == 200


def test_updated_user_schema(reqres):
    response: Response = reqres.put(url='/api/users/2', data=new_data_user_payload)

    assert S(schemas.reqres_user_schemas.updated_user_schema) == response.json()


def test_check_updated_user_new_data(reqres):
    response: Response = reqres.put(url='/api/users/2', data=new_data_user_payload)

    assert response.json()["job"] == "Author"


def test_delete_existing_user(reqres):
    response_delete = reqres.delete(url='/api/users/2')

    assert response_delete.status_code == 204
