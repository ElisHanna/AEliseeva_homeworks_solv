from pages.base_page import BasePage
from pages.product_list_page import ProductListPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    usr_name_input = (By.CSS_SELECTOR, '[name="user-name"]')
    password_input = (By.CSS_SELECTOR, '[name="password"]')
    login_bttn = (By.CSS_SELECTOR, '[name="login-button"]')
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def complete_login(self, user_name, password):
        self.send_text(self.usr_name_input, user_name)
        self.send_text(self.password_input, password)
        self.click_button(self.login_bttn)
        return ProductListPage(self.driver, self.url)

    def is_login_successful(self):
        return not self.is_element_present(self.error_message)
