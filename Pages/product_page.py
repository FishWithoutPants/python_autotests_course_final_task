from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()

    def should_match_names(self):
        product_name = self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME)
        cart_notification_name = self.get_text_from_element(*ProductPageLocators.NOTIFICATION_NAME)
        assert product_name == cart_notification_name, "Product name in notification doesn't match the product name"

    def should_match_prices(self):
        product_price = self.get_text_from_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_price = self.get_text_from_element(*ProductPageLocators.NOTIFICATION_PRICE)
        assert product_price == cart_price,\
            "Product price in notification doesn't match the product price"
