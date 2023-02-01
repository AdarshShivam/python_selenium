from SSQATest.src.SeleniumExtended import SeleniumExtended
from SSQATest.src.pages.Locators.OrderRecievedPageLocators import OrderRecievedPageLocators

class OrderRecievedPage(OrderRecievedPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_recieved_page_loaded(self):
        self.sl.wait_until_element_contains_text(self.PAGE_MAIN_HEADER, "Order received")

    def get_order_number(self):
        self.sl.wait_and_get_text(self.ORDER_NUMBER)





