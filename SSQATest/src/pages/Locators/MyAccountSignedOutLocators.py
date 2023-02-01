from selenium.webdriver.common.by import By

class MyAccountSignedOutLocators:

    LOGIN_USERNAME = (By.ID,'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR,'#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
    ERROR_UL = (By.CLASS_NAME , 'woocommerce-error')

    REGISTER_EMAIL = (By.ID , 'reg_email')
    REGISTER_PASSWORD = (By.ID , 'reg_password')
    REGISTER_BUTTON = (By.CSS_SELECTOR , 'button[value="Register"')


