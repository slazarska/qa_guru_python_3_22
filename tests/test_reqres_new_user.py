from pytest_voluptuous import S
from requests import Response

import schemas.reqres_user_schemas

new_user_payload = {
    "name": "Newton Scamander",
    "job": "Magizoologist"
}


def test_add_user(reqres):
    response: Response = reqres.post(url='/api/users', data=new_user_payload)

    assert response.status_code == 201


def test_check_added_user(reqres):
    response: Response = reqres.post(url='/api/users', data=new_user_payload)

    assert S(schemas.reqres_user_schemas.added_user_schema) == response.json()


def test_check_added_user_name(reqres):
    response: Response = reqres.post(url='/api/users', data=new_user_payload)

    assert response.json()["name"] == "Newton Scamander"


def test_added_user_job(reqres):
    response: Response = reqres.post(url='/api/users', data=new_user_payload)

    assert response.json()["job"] == "Magizoologist"