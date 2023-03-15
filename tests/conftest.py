import os

import pytest
import allure
from dotenv import load_dotenv
from selene.support.shared import browser

#from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

from framework.DemoWebShopWithEnv import DemoWebShopWithEnv

load_dotenv()


def pytest_add_option(parser):
    parser.addoption("--env", action='store', default="prod")


@pytest.fixture(scope="session")
def get_option(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def demoshop(get_option):
    return DemoWebShopWithEnv(get_option)


@pytest.fixture(scope='session')
def reqres(get_option):
    return DemoWebShopWithEnv(get_option).reqres


@pytest.fixture
def authorizated_session(demoshop):
    payload = {
        'Email': os.getenv("LOGIN"),
        'Password': os.getenv("PASSWORD")
    }

    #response = demoshop.login(os.getenv("LOGIN"), os.getenv("PASSWORD"))
    response = demoshop.post('/login', data=payload, allow_redirects=False)
    authorization_cookie = response.cookies.get('NOPCOMMERCE.AUTH')

    with allure.step("Check code"):
        response.status_code = 302

    return authorization_cookie


@pytest.fixture(scope='function')
def browser_manager(demoshop, authorization_cookie):
    #browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.config.base_url = demoshop.demoqa.url
    browser.config.window_width = 2560
    browser.config.window_height = 1440
    browser.open("/Themes/DefaultClean/Content/images/logo.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})

    yield

    browser.quit()
