import allure
from selene.support.shared import browser
from selene import have


def test_open_user_info(browser_manager):
    browser_manager.open('')

    with allure.step('Open User Info'):
        browser.element('a.account').click()
    with allure.step('Check the page with user info is opened'):
        browser.element('.page-title').should(have.text('My account - Customer info'))


def test_update_user_info(browser_manager):
    browser_manager.open('')

    with allure.step('Open User Info'):
        browser.element('a.account').click()
    with allure.step('Change the user first name'):
        browser.element('#FirstName').set_value("Testname").press_enter()
    with allure.step('Check the new user first name'):
        browser.element('#FirstName').should(have.value("Testname"))
