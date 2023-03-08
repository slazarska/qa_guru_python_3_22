import json
import logging
from json import JSONDecodeError

import allure
from curlify import to_curl
from requests import Session, Response


class BaseSession(Session):
    def __init__(self, url):
        super(BaseSession, self).__init__()
        self.url = url

    def allure_log(function):
        def wrapper(*args, **kwargs):
            method, url = args[1], args[2]
            with allure.step(f"{method} {url}"):
                response: Response = function(*args, **kwargs)

                allure.attach(body=to_curl(response.request).encode('utf8'),
                              name=f"Request: {response.status_code}",
                              attachment_type=allure.attachment_type.TEXT,
                              extension='.txt')
                try:
                    allure.attach(body=json.dumps(response.json(), indent=4),
                                  name=f"Response: {response.status_code}",
                                  attachment_type=allure.attachment_type.JSON,
                                  extension='.json')
                except JSONDecodeError:
                    allure.attach(body=response.text,
                                  name=f"Response: {response.status_code}",
                                  attachment_type=allure.attachment_type.TEXT,
                                  extension='.txt')
                return response

        return wrapper

    def rest_log(function):
        def wrapper(*args, **kwargs):
            response: Response = function(*args, **kwargs)
            logging.info(f"- code: {response.status_code} - {to_curl(response.request)}")
            return response

        return wrapper

    @rest_log
    @allure_log
    def request(self, method, url, **kwargs) -> Response:
        with allure.step(f"{method} {url}"):
            response = super().request(method, self.url + url, **kwargs)
            return response
