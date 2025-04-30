from pageObjects.LoginPage import LoginPage


class TestLogin:


    def test_login(self,browser):
        loginPage = LoginPage(browser)
        loginPage.open()
