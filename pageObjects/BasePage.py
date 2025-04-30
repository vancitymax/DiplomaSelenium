from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def _open_url(self, url):
        self._driver.get(url)

    def _find(self,locator):
        return self._driver.find_element(*locator)

    def _click(self,locator):
        self._wait_for_element_clickable(locator)
        self._find(locator).click()

    def _wait_for_element(self,locator,timeout = 10):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(visibility_of_element_located(locator))
    def _wait_for_element_clickable(self,locator,timeout = 10):
        wait = WebDriverWait(self._driver, timeout)
        wait.until(element_to_be_clickable(locator))

    def _clear(self,locator):
        self._wait_for_element(locator)
        self._find(locator).clear()

    def _type(self,locator,text):
        self._wait_for_element(locator)
        self._find(locator).send_keys(text)

    @property
    def current_url(self):
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except Exception as e:
            print(e)
            return False

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_for_element(locator, time)
        return self._find(locator).text

    def _wait_until_displayed(self, locator: tuple, time: int = 10) -> bool:
        try:
            self._wait_for_element(locator, time)
            return self._find(locator).is_displayed()
        except Exception as e:
            print(e)
            return False

