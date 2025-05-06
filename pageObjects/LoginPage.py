from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
from utilities.readProperties import ReadConfig


class LoginPage(BasePage):
    __url = 'https://www.saucedemo.com/'
    #username = ReadConfig.get_username()
    #password = ReadConfig.get_password()
    username_locator = (By.ID, 'user-name')
    password_locator = (By.ID, 'password')
    login_button_locator = (By.ID, 'login-button')
    error_message_locator = (By.XPATH,"//h3[@data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def enter_username(self, username):
        self._find(self.username_locator).send_keys(username)

    def enter_password(self, password):
        self._find(self.password_locator).send_keys(password)

    def click_login_button(self):
        self._click(self.login_button_locator)
    def get_error_message(self):
        return self._find(self.error_message_locator).text
