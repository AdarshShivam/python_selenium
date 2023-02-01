from selenium.webdriver.common.by import By

class CheckoutPageLocators:

    FIRST_NAME = (By.ID , 'billing_first_name')
    LAST_NAME = (By.ID, 'billing_last_name')

    STREET_ADDRESS = (By.ID, 'billing_address_1')
    BILLING_CITY = (By.ID, 'billing_city')
    ZIP_CODE = (By.ID, 'billing_postcode')
    PHONE = (By.ID, 'billing_phone')
    EMAIL = (By.ID, 'billing_email')

    PLACE_ORDER_BTN = (By.ID, 'place_order')
