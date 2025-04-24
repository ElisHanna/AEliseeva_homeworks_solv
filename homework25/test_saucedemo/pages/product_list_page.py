from pages.base_page import BasePage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By


class ProductListPage(BasePage):

    url =  "https://www.saucedemo.com/inventory.html"
    add_bttns = (By.CSS_SELECTOR, '[class="btn btn_primary btn_small btn_inventory "]')
    rm_bttn1 = (By.CSS_SELECTOR, '[name="remove-sauce-labs-onesie"]')
    rm_bttn2 = (By.CSS_SELECTOR, '[name="remove-test.allthethings()-t-shirt-(red)"]')
    cart_bttn = (By.CSS_SELECTOR, '[class="shopping_cart_link"]')


    def __init__(self, driver, url):
        super().__init__(driver, url=url)

    def add_to_cart(self, number):
        self.check_number(self.add_bttns, number)
        self.click_buttons(self.add_bttns)

    def remove(self):
        self.click_button(self.rm_bttn1)
        self.click_button(self.rm_bttn2)

    def go_to_cart(self):
        self.click_button(self.cart_bttn)
        return CartPage(self.driver, self.url)
