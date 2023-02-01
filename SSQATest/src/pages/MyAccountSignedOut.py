from SSQATest.src.pages.Locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from SSQATest.src.SeleniumExtended import SeleniumExtended
from SSQATest.src.helpers.config_helpers import get_base_url

import logging as logger

class MyAccountSignedOut(MyAccountSignedOutLocators):
    endpoint = '/my-account'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)
        logger.info(f"Going to {my_account_url}")

    def input_login_username(self ,username):
        self.sl.wait_and_input_text(self.LOGIN_USERNAME,username)

    def input_login_password(self , password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def onclick_login_button(self):
        logger.debug("Clicking 'login' button")
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERROR_UL , exp_err)

    def input_register_email(self ,email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL,email)

    def input_register_password(self , password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def onclick_register_button(self):
        logger.debug("Clicking 'Register' button")
        self.sl.wait_and_click(self.REGISTER_BUTTON)

