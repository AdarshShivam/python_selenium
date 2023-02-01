from SSQATest.src.helpers.config_helpers import get_base_url
from SSQATest.src.SeleniumExtended import SeleniumExtended
from SSQATest.src.pages.Locators.HomePageLocators import HomePageLocators
import logging as logger

class HomePage(HomePageLocators):

    def __init__(self,driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def add_item_to_cart(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)
        logger.debug('Adding item to cart')