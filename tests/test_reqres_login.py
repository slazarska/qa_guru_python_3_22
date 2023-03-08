from pytest_voluptuous import S
from requests import Response

import schemas.reqres_login_schemas

valid_creds_payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

invalid_creds_payload = {
    "email": "peter@klaven"
}


def test_successful_login(reqres):
    response: Response = reqres.post(url='/api/login', data=valid_creds_payload)

    assert response.status_code == 200
    assert S(schemas.reqres_login_schemas.login_pass_schema) == response.json()


def test_check_token_successful_login(reqres):
    response: Response = reqres.post(url='/api/login', data=valid_creds_payload)

    assert response.json()["token"] == "QpwL5tke4Pnpja7X4"


def test_login_with_error(reqres):
    response: Response = reqres.post(url='/api/login', data=invalid_creds_payload)

    assert response.status_code == 400
    assert S(schemas.reqres_login_schemas.login_fail_schema) == response.json()


def test_check_login_error(reqres):
    response: Response = reqres.post(url='/api/login', data=invalid_creds_payload)

    assert response.json()["error"] == "Missing password"