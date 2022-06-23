from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_CART_BTN = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, '[name = "registration-email"]')
    REGISTER_FORM_PASSWORD_FIELD_1 = (By.CSS_SELECTOR, '[name = "registration-password1"]')
    REGISTER_FORM_PASSWORD_FIELD_2 = (By.CSS_SELECTOR, '[name = "registration-password2"]')
    REGISTER_FORM_SUBMIT_BTN = (By.CSS_SELECTOR, '[name = "registration_submit"]')


class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    NOTIFICATION_PRICE = (By.CSS_SELECTOR, '.alertinner > p > strong')
    NOTIFICATION_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_ALERT = (By.CSS_SELECTOR, "#content_inner > p")

