from pages.base_page import BasePage

class LogoutPage(BasePage):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver, url):
        super().__init__(driver, url=url)
