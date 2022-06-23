from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        link.click()

    def should_match_names(self):
        product_name = self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME)
        notification_name = self.get_text_from_element(*ProductPageLocators.NOTIFICATION_NAME)
        assert product_name == notification_name, f"Product name in notification doesn't match the product name. \
        Expected {product_name}, got {notification_name}"

    def should_match_prices(self):
        product_price = self.get_text_from_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_price = self.get_text_from_element(*ProductPageLocators.NOTIFICATION_PRICE)
        assert product_price == cart_price,\
            f"Product price in notification doesn't match the product price. Expected {product_price}, got {cart_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should have disappear"

