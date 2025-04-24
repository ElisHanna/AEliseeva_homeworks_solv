from selenium.common.exceptions import NoSuchElementException


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

    def click_button(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def click_buttons(self, locator):
        buttons = self.driver.find_elements(*locator)
        for button in buttons:
            button.click()

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
