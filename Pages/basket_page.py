from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
                "Basket item is presented, but should not be"

    def should_be_a_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_ALERT), \
                "Empty basket alert is not presented"
