from pages.base_page import BasePage
from pages.logout_page import LogoutPage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    url = 'https://www.saucedemo.com/inventory.html'
    hidden_menu_bttn = (By.CSS_SELECTOR, '[id="react-burger-menu-btn"]')
    logout_bttn = (By.CSS_SELECTOR, '[id="logout_sidebar_link"]')

    def __init__(self, driver, url):
        super().__init__(driver, url=url)

    def logout(self):
        self.click_button(self.hidden_menu_bttn)
        self.click_button(self.logout_bttn)
        return LogoutPage(self.driver, self.url)
