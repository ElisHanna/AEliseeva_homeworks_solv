from pages.base_page import BasePage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By


class CompletePage(BasePage):

    url = 'https://www.saucedemo.com/checkout-complete.html'
    home_bttn = (By.CSS_SELECTOR, '[name="back-to-products"]')

    def __init__(self, driver, url):
        super().__init__(driver, url=url)

    def go_home(self):
        self.click_button(self.home_bttn)
        return HomePage(self.driver, self.url)
