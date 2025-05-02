from pages.base_page import BasePage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    url = "https://www.saucedemo.com/cart.html"
    rm_bttn1 = (By.CSS_SELECTOR, '[name="remove-sauce-labs-fleece-jacket"]')
    rm_bttn2 = (By.CSS_SELECTOR, '[name="remove-sauce-labs-backpack"]')
    goods = (By.CSS_SELECTOR, '[class="cart_item"]')
    checkout_bttn = (By.CSS_SELECTOR, '[name="checkout"]')

    def __init__(self, driver, url):
        super().__init__(driver, url=url)

    def remove_from_cart(self, num_before, num_after):
        self.check_number(self.goods, num_before)
        self.click_button(self.rm_bttn1)
        self.click_button(self.rm_bttn2)
        self.check_number(self.goods, num_after)

    def checkout(self):
        self.click_button(self.checkout_bttn)
        return CheckoutPage(self.driver, self.url)
