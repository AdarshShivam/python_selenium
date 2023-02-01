from SSQATest.src.pages.Locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from SSQATest.src.SeleniumExtended import SeleniumExtended
import logging as logger

class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def onclick_logout_button(self):
        logger.debug("Clicking 'Log Out' button")
        self.sl.wait_until_element_visible(self.SIDE_VIEW_LOGOUT_BUTTON)
