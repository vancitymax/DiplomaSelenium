import pytest

from pageObjects.LoginPage import LoginPage


class TestLogin:

    @pytest.mark.login
    @pytest.mark.validLogin
    def test_login_with_valid_data(self,browser):
        loginPage = LoginPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()

    @pytest.mark.login
    @pytest.mark.invalidLogin
    @pytest.mark.parametrize("login,password,errorMessage",[("standard_user","secret_sauce123","Username and password do not match any user in this service"),("standard_user123","secret_sauce","Username and password do not match any user in this service")])
    def test_login_with_invalid_data(self,browser,login,password,errorMessage):
        loginPage = LoginPage(browser)
        loginPage.open()
        loginPage.enter_username(login)
        loginPage.enter_password(password)
        loginPage.click_login_button()
        assert errorMessage in loginPage.get_error_message()
