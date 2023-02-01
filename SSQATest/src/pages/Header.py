from SSQATest.src.SeleniumExtended import SeleniumExtended
from SSQATest.src.pages.Locators.HeaderLocators import HeaderLocators
import logging as logger

class Header(HeaderLocators):

    def __init__(self , driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def wait_until_cart_item_count(self, count):
        expected_text = str(count) + ' item'
        self.sl.wait_until_element_contains_text(self.RIGHT_CART_TEXT ,expected_text)
        logger.debug(expected_text)

    def click_on_cart_on_right_header(self):
        self.sl.wait_and_click(self.RIGHT_CART_BTN)

