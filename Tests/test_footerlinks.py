import pytest

from Tests.conftest import browser
from pageObjects.FooterLink import FooterLinkPage
from pageObjects.LoginPage import LoginPage


class TestFooterLinks:
    @pytest.mark.footerlinks
    def test_footer_link_to_linkedin(self,browser):
        loginPage = LoginPage(browser)
        footerLinks = FooterLinkPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        footerLinks.navigate_to_linkedin()

    @pytest.mark.footerlinks
    def test_footer_link_to_facebook(self,browser):
        loginPage = LoginPage(browser)
        footerLinks = FooterLinkPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        footerLinks.navigate_to_facebook()

    @pytest.mark.footerlinks
    def test_footer_link_to_twitter(self,browser):
        loginPage = LoginPage(browser)
        footerLinks = FooterLinkPage(browser)
        loginPage.open()
        loginPage.enter_username("standard_user")
        loginPage.enter_password("secret_sauce")
        loginPage.click_login_button()
        footerLinks.navigate_to_twitter()