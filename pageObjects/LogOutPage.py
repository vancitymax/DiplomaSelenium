from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class LogOutPage(BasePage):
    logout_button = (By.ID,'logout_sidebar_link')

    def __init__(self, driver):
        super().__init__(driver)


    def click_logout_button(self):
        self._click(self.logout_button)

