import allure
from selene.support.shared import browser
from selene import have


def test_add_to_shopping_cart(browser_manager):
    browser_manager.open('')

    with allure.step('Choose the laptop'):
        browser.open('/141-inch-laptop')
    with allure.step('Adding the choosed laptop to the shopping cart'):
        browser.element('.add-to-cart-button').click()
    with allure.step('Open the shopping cart'):
        browser.element('.ico-cart .cart-label').click()
    with allure.step('Check the shopping cart is not empty'):
        browser.element('.cart-qty').should(have.text('1'))
    with allure.step('Delete the laptop from the shopping cart'):
        browser.element('.qty-input').clear().set_value('0')
        browser.element('.update-cart-button').click()


def test_delete_from_shopping_cart(browser_manager):
    browser_manager.open('')

    with allure.step('Choose the laptop'):
        browser.open('/141-inch-laptop')
    with allure.step('Adding the choosed laptop to the shopping cart'):
        browser.element('.add-to-cart-button').click()
    with allure.step('Open the shopping cart'):
        browser.element('.ico-cart .cart-label').click()
    with allure.step('Delete the laptop from the shopping cart'):
        browser.element('.qty-input').clear().set_value('0')
        browser.element('.update-cart-button').click()
    with allure.step('Check the shopping cart is empty'):
        browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def test_change_the_count_of_product_in_the_shopping_cart(browser_manager):
    browser_manager.open('')

    with allure.step('Choose the laptop'):
        browser.open('/141-inch-laptop')
    with allure.step('Adding the choosed laptop to the shopping cart'):
        browser.element('.add-to-cart-button').click()
    with allure.step('Open the shopping cart'):
        browser.element('.ico-cart .cart-label').click()
    with allure.step('Delete the laptop fro the shopping cart'):
        browser.element('.qty-input').clear().set_value('2')
        browser.element('.update-cart-button').click()
    with allure.step('Check the count of the product is increased'):
        browser.element('.cart-qty').should(have.text('2'))
    with allure.step('Delete the laptop from the shopping cart'):
        browser.element('.qty-input').clear().set_value('0')
        browser.element('.update-cart-button').click()
