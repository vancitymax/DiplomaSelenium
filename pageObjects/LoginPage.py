from pageObjects.BasePage import BasePage
from utilities.readProperties import ReadConfig


class LoginPage(BasePage):
    __url = ''
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    def __init__(self, driver):
        super().__init__()

    def open(self):
        super()._open_url(self.__url)