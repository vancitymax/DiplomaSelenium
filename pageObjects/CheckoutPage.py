from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class CheckoutPage(BasePage):
    checkout_button = (By.ID,'checkout')
    remove_button = (By.ID,'remove-sauce-labs-backpack')
    first_name_locator = (By.ID,'first-name')
    last_name_locator = (By.ID,'last-name')
    postal_code_locator = (By.ID,'postal-code')
    continue_locator = (By.ID,'continue')
    finish_locator = (By.ID,'finish')
    complete_header_locator = (By.CLASS_NAME,'complete-header')
    back_home_locator = (By.ID,'back-to-products')
    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout(self):
        self._click(self.checkout_button)

    def enter_last_name(self,name):
        self._find(self.last_name_locator).send_keys(name)

    def enter_postal_code(self,postal_code):
        self._find(self.postal_code_locator).send_keys(postal_code)

    def enter_first_name(self,first_name):
        self._find(self.first_name_locator).send_keys(first_name)

    def click_continue(self):
        self._click(self.continue_locator)

    def click_finish(self):
        self._click(self.finish_locator)

    def get_confirmation_text(self):
        return self._find(self.complete_header_locator).text


