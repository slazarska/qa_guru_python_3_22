import pytest
from allure_commons._allure import step
from selene.support.shared import browser
from selene import have
from flaky import flaky


@flaky(max_runs=3, min_passes=1)
def test_add_to_shopping_cart(authorizated_session, demoshop):
    browser.open('')

    with step('Choose the laptop'):
        browser.open('/141-inch-laptop')
    with step('Adding the choosed laptop to the shopping cart'):
        browser.element('.add-to-cart-button').click()
    with step('Open the shopping cart'):
        browser.element('.ico-cart .cart-label').click()
    with step('Check the shopping cart is not empty'):
        browser.element('.cart-qty').should(have.text('1'))


def test_delete_from_shopping_cart(authorizated_session, demoshop):
    browser.open('')

    with step('Choose the laptop'):
        browser.open('/141-inch-laptop')
    with step('Adding the choosed laptop to the shopping cart'):
        browser.element('.add-to-cart-button').click()
    with step('Open the shopping cart'):
        browser.element('.ico-cart .cart-label').click()
    with step('Delete the laptop from the shopping cart'):
        browser.element('.qty-input').clear().set_value('0')
        browser.element('.update-cart-button').click()
    with step('Check the shopping cart is empty'):
        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_change_the_count_of_product_in_the_shopping_cart(authorizated_session, clean_the_shopping_cart, demoshop):
    browser.open('')

    with step('Choose the laptop'):
        browser.open('/141-inch-laptop')
    with step('Adding the choosed laptop to the shopping cart'):
        browser.element('.add-to-cart-button').click()
    with step('Open the shopping cart'):
        browser.element('.ico-cart .cart-label').click()
    with step('Delete the laptop fro the shopping cart'):
        browser.element('.qty-input').clear().set_value('2')
        browser.element('.update-cart-button').click()
    with step('Check the count of the product is increased'):
        browser.element('.cart-qty').should(have.text('2'))
