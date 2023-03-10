import os

import pytest
from allure_commons._allure import step
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from framework.DemoWebShopWithEnv import DemoWebShopWithEnv

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
SHOP_URL = os.getenv('API_DEMOWEBSHOP')


def pytest_addoption(parser):
    parser.addoption("--env")


@pytest.fixture(scope='session')
def demoshop(request):
    env = request.config.getoption("--env")
    return DemoWebShopWithEnv(env)


@pytest.fixture(scope='session')
def reqres(request):
    env = request.config.getoption("--env")
    return DemoWebShopWithEnv(env).reqres


@pytest.fixture
def authorizated_session(demoshop):
    browser.config.base_url = SHOP_URL
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    browser.config.window_width = 2560
    browser.config.window_height = 1440

    payload = {
        'Email': LOGIN,
        'Password': PASSWORD
    }

    response = demoshop.post('/login', data=payload, allow_redirects=False)
    cookies = response.cookies.get('NOPCOMMERCE.AUTH')

    with step("Check code"):
        response.status_code = 302

    browser.open('/Themes/DefaultClean/Content/images/logo.png')
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookies})

    yield

    browser.quit()
