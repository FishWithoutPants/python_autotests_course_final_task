from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    NOTIFICATION_PRICE = (By.CSS_SELECTOR, '.alertinner > p > strong')
    NOTIFICATION_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
