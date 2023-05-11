import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

class SeleniumExtended:

    def __init__(self , driver):
        self.driver = driver
        self.default_timeout = 12

    def wait_and_input_text(self , locator , text ,timeout=None):
        timeout = timeout if timeout else self.default_timeout

        if locator is "CSS_SELECTOR":
            WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator).send_keys())

        else:
            input_field = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_any_elements_located(locator))
            input_field[0].send_keys(text)

    def wait_and_click(self, locator , timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
            ).click()

        except StaleElementReferenceException:
            time.sleep(2)
            # sleeping and trying again
            WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
            ).click()

    def wait_until_element_contains_text(self , locator, text, timeout=None):

            timeout = timeout if timeout else self.default_timeout

            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator,text)
            )

    def wait_and_select_checkbox(self, locator, timeout=None):

        timeout = timeout if timeout else self.default_timeout
        # try:
        WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()

        # except StaleElementReferenceException:
        #     time.sleep(2)
        #     # sleeping and trying again
        #     WebDriverWait(self.driver, timeout).until(
        #         EC.element_to_be_clickable(locator)
        #     ).click()

    def wait_until_element_visible(self , locator , timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
            )

    def wait_and_get_elements(self , locator, timeout=None, err=None):

        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"Unable to find elements located by {locator},"\
                              f"after timeout of {timeout}"
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )

        except TimeoutException:
            raise TimeoutException(err)

        return element

    def wait_and_get_text(self, locator , timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text

        return element_text

    def wait_and_select_dropdown(self, locator, timeout=None):

        timeout = timeout if timeout else self.default_timeout

        dropdown_button = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        dropdown_button.click()
        time.sleep(2)
        dropdown_button.send_keys(Keys.ARROW_DOWN)
        dropdown_button.send_keys(Keys.ENTER)

    def wait_and_select_dropdown_non_api(self, locator, timeout=None):

        timeout = timeout if timeout else self.default_timeout

        dropdown_button = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        dropdown_button.click()
        dropdown_button.send_keys(Keys.ARROW_DOWN)
        dropdown_button.send_keys(Keys.ENTER)

    def select_desired_value_from_dropdown(self, locator, text, timeout=None):

        timeout = timeout if timeout else self.default_timeout

        new_dropdown_button = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        new_dropdown_button.click()

        new_dropdown_button.send_keys(text)
        new_dropdown_button.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)
        new_dropdown_button.send_keys(Keys.ENTER)

    def wait_and_select_date(self, locator, date, year, timeout=None):

        timeout = timeout if timeout else self.default_timeout

        if locator is "CSS_SELECTOR" :
            date_selector_css = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
            date_selector_css.send_keys(date)
            date_selector_css.send_keys(Keys.TAB)
            date_selector_css.send_keys(year)
        else:
            date_selector = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_any_elements_located(locator))
            date_selector[0].send_keys(date)
            date_selector[0].send_keys(Keys.TAB)
            date_selector[0].send_keys(year)

    def wait_and_clear_field_and_input_value(self,locator,value, timeout=None):

        timeout = timeout if timeout else self.default_timeout

        if locator is "CSS_SELECTOR":
            time.sleep(2)
            filled_field_css = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

            filled_field_css.send_keys(Keys.CONTROL + "a")
            filled_field_css.send_keys(Keys.DELETE)
            filled_field_css.send_keys(value)

        else:
            time.sleep(2)
            filled_field = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_any_elements_located(locator))

            filled_field[0].send_keys(Keys.CONTROL + "a")
            filled_field[0].send_keys(Keys.DELETE)
            filled_field[0].send_keys(value)

        # time.sleep(2)
        # filled_field = WebDriverWait(self.driver, timeout).until(
        #     EC.visibility_of_element_located(locator))
        #
        # filled_field.send_keys(Keys.CONTROL + "a")
        # filled_field.send_keys(Keys.DELETE)
        # filled_field.send_keys(value)

    def wait_and_select_mrp_dropdown(self, locator, timeout=None):

        timeout = timeout if timeout else self.default_timeout

        dropdown_button = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        time.sleep(2)
        dropdown_button.send_keys(Keys.ARROW_DOWN)
        dropdown_button.send_keys(Keys.ENTER)

    def wait_for_ajax(self):

        wait = WebDriverWait(self, self.default_timeout)
        print("all ok")
        try:
            wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
            wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        except Exception as e:
            pass

