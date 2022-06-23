from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "Current url is not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def press_register_button(self):
        btn = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_SUBMIT_BTN)
        btn.click()

    def register_new_user(self, email, password):
        self.go_to_login_page()
        self.input_text_to_field(*LoginPageLocators.REGISTER_FORM_EMAIL_FIELD, email)
        self.input_text_to_field(*LoginPageLocators.REGISTER_FORM_PASSWORD_FIELD_1, password)
        self.input_text_to_field(*LoginPageLocators.REGISTER_FORM_PASSWORD_FIELD_2, password)
        self.press_register_button()
