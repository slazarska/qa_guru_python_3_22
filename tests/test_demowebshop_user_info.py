from allure_commons._allure import step
from selene.support.shared import browser
from selene import have


def test_open_user_info(authorizated_session, demoshop):
    browser.open('')

    with step('Open User Info'):
        browser.element('a.account').click()
    with step('Check the page with user info is opened'):
        browser.element('.page-title').should(have.text('My account - Customer info'))


def test_update_user_info(authorizated_session, demoshop):
    browser.open('')

    with step('Open User Info'):
        browser.element('a.account').click()
    with step('Change the user first name'):
        browser.element('#FirstName').set_value("Testname").press_enter()
    with step('Check the new user first name'):
        browser.element('#FirstName').should(have.value("Testname"))
