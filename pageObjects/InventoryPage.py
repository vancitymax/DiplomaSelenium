from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage


class InventoryPage(BasePage):
    burger_menu_locator = (By.ID,'react-burger-menu-btn')
    bm_menu_locator = (By.CLASS_NAME,'bm-menu')
    cart_locator = (By.CLASS_NAME,'shopping_cart_link')
    add_to_cart_locator = (By.ID,"add-to-cart-sauce-labs-backpack")
    cart_badge_locator = (By.CLASS_NAME,'shopping_cart_badge')
    sort_dropdown = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')
    product_prices = (By.CLASS_NAME, 'inventory_item_price')
    product_names = (By.CLASS_NAME, 'inventory_item_name')
    def __init__(self, driver):
        super().__init__(driver)


    def burger_menu_is_displayed(self):
        self._is_displayed(self.bm_menu_locator)

    def click_burger_menu(self):
        self._click(self.burger_menu_locator)

    def click_cart(self):
        self._click(self.cart_locator)
    def add_product_to_cart(self):
        self._find(self.add_to_cart_locator).click()

    def verify_product_in_cart(self):
       return self._find(self.cart_locator).text

    def select_sort_option(self, option_text):
        from selenium.webdriver.support.ui import Select
        select_element = self._find(self.sort_dropdown)  # Повертає один елемент
        select = Select(select_element)
        select.select_by_visible_text(option_text)

    def get_product_prices(self):
        prices = self._find_all(self.product_prices)
        return [float(p.text.replace('$', '')) for p in prices]

    def get_product_names(self):
        names = self._find_all(self.product_names)
        return [n.text.strip() for n in names]


