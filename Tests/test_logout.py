from threading import Thread

from pageObjects.InventoryPage import InventoryPage
from pageObjects.LogOutPage import LogOutPage
from pageObjects.LoginPage import LoginPage
import pytest

class TestLogout:

    @pytest.mark.logout
    def test_logout(self,browser):
        loginPage = LoginPage(browser)
        inventoryPage = InventoryPage(browser)
        logoutPage = LogOutPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        inventoryPage.click_burger_menu()
        logoutPage.click_logout_button()


