from SSQATest.src.SeleniumExtended import SeleniumExtended
from SSQATest.src.pages.Locators.CheckoutPageLocators import CheckoutPageLocators
from SSQATest.src.helpers.generic_helpers import generate_random_email_and_password
import json

class data_from_json():
    # read
    file = open('json_files/(file_name).json', 'r')
    # data = file.read()
    # parse
    obj = json.load(file)
    list_value = obj['test1']
    # Iterating through json list
    for keys in list_value:
        data = keys

class Checkout(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name else 'AutomationFname'
        self.sl.wait_and_input_text(self.FIRST_NAME, first_name)

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name else 'AutomationLname'
        self.sl.wait_and_input_text(self.LAST_NAME, last_name)

    def input_street_address(self, address=None):
        address = address if address else '123StreetAddress'
        self.sl.wait_and_input_text(self.STREET_ADDRESS, address)

    def input_billing_city(self, city=None):
        city = city if city else 'San Francisco'
        self.sl.wait_and_input_text(self.BILLING_CITY, city)

    def input_zipcode(self, zipcode=None):
        zipcode = zipcode if zipcode else '94015'
        self.sl.wait_and_input_text(self.ZIP_CODE, zipcode)

    def input_phone_number(self, phone_number=None):
        phone_number = phone_number if phone_number else '1234567890'
        self.sl.wait_and_input_text(self.PHONE, phone_number)

    def input_email(self, billing_email=None):

        if not billing_email:
            rand_email = generate_random_email_and_password()
            billing_email = rand_email
            self.sl.wait_and_input_text(self.EMAIL, billing_email)

    def fill_in_billing_info(self,first_name=None,last_name=None, address=None,city=None,zipcode=None,phone_number=None,email=None ):
        self.input_billing_first_name(first_name=first_name)
        self.input_billing_last_name(last_name=last_name)
        self.input_street_address(address=address)
        self.input_billing_city(city=city)
        self.input_zipcode(zipcode=zipcode)
        self.input_phone_number(phone_number=phone_number)
        self.input_email(billing_email=email)

    def click_place_order_btn(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)