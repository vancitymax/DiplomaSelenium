from pageObjects.InventoryPage import InventoryPage
from pageObjects.LoginPage import LoginPage


class TestSorting:
    def test_sort_price_low_to_high(self, browser):
        page = InventoryPage(browser)
        loginPage = LoginPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        page.select_sort_option("Price (low to high)")
        prices = page.get_product_prices()
        assert prices == sorted(prices)

    def test_sort_price_high_to_low(self, browser):
        page = InventoryPage(browser)
        loginPage = LoginPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        page.select_sort_option("Price (high to low)")
        prices = page.get_product_prices()
        assert prices == sorted(prices, reverse=True)

    def test_sort_name_a_to_z(self, browser):
        loginPage = LoginPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        page = InventoryPage(browser)
        page.select_sort_option("Name (A to Z)")
        names = page.get_product_names()
        assert names == sorted(names)

    def test_sort_name_z_to_a(self, browser):
        loginPage = LoginPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        page = InventoryPage(browser)
        page.select_sort_option("Name (Z to A)")
        names = page.get_product_names()
        assert names == sorted(names, reverse=True)