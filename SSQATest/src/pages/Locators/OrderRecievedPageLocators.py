from selenium.webdriver.common.by import By

class OrderRecievedPageLocators:

    PAGE_MAIN_HEADER = (By.CSS_SELECTOR,'header h1.entry-title')

    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.order strong')
