import pytest

from pageObjects.BasePage import BasePage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.InventoryPage import InventoryPage
from pageObjects.LoginPage import LoginPage


class TestCartPage:

    @pytest.mark.addToCartPage
    def test_add_to_cart(self,browser):
        loginPage = LoginPage(browser)
        inventoryPage = InventoryPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        inventoryPage.add_product_to_cart()
        assert inventoryPage.verify_product_in_cart() == '1'

    def test_checkout(self,browser):
        loginPage = LoginPage(browser)
        inventoryPage = InventoryPage(browser)
        checkoutPage = CheckoutPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        inventoryPage.add_product_to_cart()
        inventoryPage.click_cart()
        checkoutPage.click_checkout()
        checkoutPage.enter_first_name("Max")
        checkoutPage.enter_last_name("Palamarchuk")
        checkoutPage.enter_postal_code(16600)
        checkoutPage.click_continue()
        checkoutPage.click_finish()
        assert checkoutPage.get_confirmation_text() == 'Thank you for your order!'



