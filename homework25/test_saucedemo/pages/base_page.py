from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def send_text(self, locator, text):
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)

    def click_button(self, locator, timeout=10):
        button = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        button.click()

    def click_buttons(self, locator, timeout=10):
        buttons = self.driver.find_elements(*locator)
        for btn in buttons:
            clc_button = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(btn))
            clc_button.click()

    def check_number(self, locator, number):
        items_list = self.driver.find_elements(*locator)
        assert len(items_list) == number

    def is_current_url(self, url):
        return self.driver.current_url == url, \
               f"Expected to get {url} but got {self.driver.current_url}"

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
