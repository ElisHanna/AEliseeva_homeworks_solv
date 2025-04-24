from pages.base_page import BasePage
from pages.checkout_complete_page import CompletePage
from selenium.webdriver.common.by import By


class OverwiewPage(BasePage):

    url = 'https://www.saucedemo.com/checkout-step-two.html'
    goods = (By.CSS_SELECTOR, '[class="cart_item"]')
    fin_bttn = (By.CSS_SELECTOR, '[name="finish"]')

    def __init__(self, driver, url):
        super().__init__(driver, url=url)

    def finish(self, number):
        self.check_number(self.goods, number)
        self.click_button(self.fin_bttn)
        return CompletePage(self.driver, self.url)
