from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class FooterLinkPage(BasePage):
    linkedin_locator = (By.LINK_TEXT,'LinkedIn')
    facebook_locator = (By.LINK_TEXT,'Facebook')
    twitter_locator = (By.LINK_TEXT,'Twitter')

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_linkedin(self):
         self._click(self.linkedin_locator)

    def navigate_to_facebook(self):
        self._click(self.facebook_locator)
    def navigate_to_twitter(self):
        self._click(self.twitter_locator)


