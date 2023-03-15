import os

import allure
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


def test_demowebshop_successful_login(browser_manager):
    browser_manager.open("")

    with allure.step("Check successful authorization in Response"):
        assert browser_manager.status_code == 302
    with allure.step("Check successful authorization on UI"):
        browser_manager.element(".account").should(have.text(LOGIN))


def test_logout(browser_manager):
    browser_manager.open("")

    with allure.step("Logout"):
        browser.element('.ico-logout').click()
    with allure.step("Check successful logout on in Response"):
        assert browser_manager.status_code == 302
    with allure.step("Check successful logout on UI"):
        browser.element('.ico-login').should(have.text('Log in'))
