from selenium.webdriver.common.by import By

class HeaderLocators:

    RIGHT_CART_BTN = (By.ID , 'site-header-cart')
    RIGHT_CART_TEXT = (By.CSS_SELECTOR , 'ul#site-header-cart span.count')
