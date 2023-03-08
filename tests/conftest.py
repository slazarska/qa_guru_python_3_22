import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils.base_session import BaseSession

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
SHOP_URL = os.getenv('API_DEMOWEBSHOP')


@pytest.fixture(scope="session")
def reqres():
    api_url = os.getenv("API_REQRES")
    return BaseSession(api_url)


@pytest.fixture(scope="session")
def demoshop():
    api_url = os.getenv("API_DEMOWEBSHOP")
    return BaseSession(api_url)


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

    browser.open('/Themes/DefaultClean/Content/images/logo.png')
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookies})

    yield

   # browser.quit()


@pytest.fixture()
def clean_the_shopping_cart():
    yield
    browser.element('.qty-input').clear().set_value('0')
    browser.element('.update-cart-button').click()
