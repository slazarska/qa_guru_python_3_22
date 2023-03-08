import os

from allure_commons._allure import step
from dotenv import load_dotenv
from selene import have
from selene.support.shared import browser

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')


def test_demowebshop_successful_login(demoshop):
    response = demoshop.post("/login",
                             json={"Email": LOGIN, "Password": PASSWORD},
                             allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("https://demowebshop.tricentis.com/")

    browser.driver.add_cookie({'name': "NOPCOMMERCE.AUTH", 'value': authorization_cookie})
    browser.open("https://demowebshop.tricentis.com/")

    with step("Check successful authorization in Response"):
        assert response.status_code == 302
    with step("Check successful authorization on UI"):
        browser.element(".account").should(have.text(LOGIN))


def test_logout(demoshop):
    response = demoshop.post("/login",
                             json={"Email": LOGIN, "Password": PASSWORD},
                             allow_redirects=False)
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    browser.open("https://demowebshop.tricentis.com/")

    browser.driver.add_cookie({'name': "NOPCOMMERCE.AUTH", 'value': authorization_cookie})
    browser.open("https://demowebshop.tricentis.com/")

    with step("Logout"):
        browser.element('.ico-logout').click()
    with step("Check successful logout on in Response"):
        assert response.status_code == 302
    with step("Check successful logout on UI"):
        browser.element('.ico-login').should(have.text('Log in'))
