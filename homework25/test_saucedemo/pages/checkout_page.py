from pages.base_page import BasePage
from pages.checkout_overwiew_page import OverwiewPage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):

    url = "https://www.saucedemo.com/checkout-step-one.html"
    f_name_input = (By.CSS_SELECTOR, '[name="firstName"]')
    l_name_input = (By.CSS_SELECTOR, '[name="lastName"]')
    zipcode_input = (By.CSS_SELECTOR, '[name="postalCode"]')
    continue_link = (By.CSS_SELECTOR, '[name="continue"]')

    def __init__(self, driver, url):
        super().__init__(driver, url=url)

    def fill_postal_data(self, name, last_name, zipcode):
        self.send_text(self.f_name_input, name)
        self.send_text(self.l_name_input, last_name)
        self.send_text(self.zipcode_input, zipcode)
        self.click_button(self.continue_link)
        return OverwiewPage(self.driver, self.url)
