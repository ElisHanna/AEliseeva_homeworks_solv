import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.close()


@pytest.fixture
def login(driver):
    driver.get('https://www.saucedemo.com/')
    usr_name_input = driver.find_element(By.CSS_SELECTOR, '[name="user-name"]')
    usr_name_input.clear()
    usr_name_input.send_keys('standard_user')
    password_input = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
    password_input.clear()
    password_input.send_keys('secret_sauce')
    login_bttn = driver.find_element(By.CSS_SELECTOR, '[name="login-button"]')
    login_bttn.click()


def test_bying(driver, login):
    inventory_url = driver.current_url
    assert inventory_url == "https://www.saucedemo.com/inventory.html", \
                            f'Wrong URL {inventory_url}'
    add_bttns = driver.find_elements(By.CSS_SELECTOR,
                                     '[class="btn btn_primary btn_small btn_inventory "]')
    assert len(add_bttns) == 6
    for bttn in add_bttns:
        bttn.click()
    rm_bttn1 = driver.find_element(By.CSS_SELECTOR, '[name="remove-sauce-labs-onesie"]')
    rm_bttn1.click()
    rm_bttn2 = driver.find_element(By.CSS_SELECTOR,
                               '[name="remove-test.allthethings()-t-shirt-(red)"]')
    rm_bttn2.click()
    cart_bttn = driver.find_element(By.CSS_SELECTOR, '[class="shopping_cart_link"]')
    cart_bttn.click()
    cart_url = driver.current_url
    assert cart_url == "https://www.saucedemo.com/cart.html", f'Wrong URL {cart_url}'
    cart_list = driver.find_elements(By.CSS_SELECTOR, '[class="cart_item"]')
    assert len(cart_list) == 4
    rm_bttn3 = driver.find_element(By.CSS_SELECTOR, '[name="remove-sauce-labs-fleece-jacket"]')
    rm_bttn3.click()
    rm_bttn4 = driver.find_element(By.CSS_SELECTOR, '[name="remove-sauce-labs-backpack"]')
    rm_bttn4.click()
    new_cart_list = driver.find_elements(By.CSS_SELECTOR, '[class="cart_item"]')
    assert len(new_cart_list) == 2
    checkout_bttn = driver.find_element(By.CSS_SELECTOR, '[name="checkout"]')
    checkout_bttn.click()
    checkout_url = driver.current_url
    assert checkout_url == "https://www.saucedemo.com/checkout-step-one.html", \
                           f'Wrong URL {checkout_url}'
    f_name_input = driver.find_element(By.CSS_SELECTOR, '[name="firstName"]')
    f_name_input.clear()
    f_name_input.send_keys('John')
    l_name_input = driver.find_element(By.CSS_SELECTOR, '[name="lastName"]')
    l_name_input.clear()
    l_name_input.send_keys('Walker')
    zipcode_input = driver.find_element(By.CSS_SELECTOR, '[name="postalCode"]')
    zipcode_input.clear()
    zipcode_input.send_keys('212850')
    continue_link = driver.find_element(By.CSS_SELECTOR, '[name="continue"]')
    continue_link.click()
    continue_url = driver.current_url
    assert continue_url == 'https://www.saucedemo.com/checkout-step-two.html', \
                           f'Wrong URL {continue_url}'
    finish_list = driver.find_elements(By.CSS_SELECTOR, '[class="cart_item"]')
    assert len(finish_list) == 2
    fin_bttn = driver.find_element(By.CSS_SELECTOR, '[name="finish"]')
    fin_bttn.click()
    fin_url = driver.current_url
    assert fin_url == 'https://www.saucedemo.com/checkout-complete.html', f'Wrong URL {fin_url}'
    home_bttn = driver.find_element(By.CSS_SELECTOR, '[name="back-to-products"]')
    home_bttn.click()
    home_url = driver.current_url
    assert home_url == 'https://www.saucedemo.com/inventory.html', f'Wrong URL {home_url}'
    hidden_menu_bttn = driver.find_element(By.CSS_SELECTOR, '[id="react-burger-menu-btn"]')
    hidden_menu_bttn.click()
    logout_bttn = driver.find_element(By.CSS_SELECTOR, '[id="logout_sidebar_link"]')
    logout_bttn.click()
    logout_url = driver.current_url
    assert logout_url == 'https://www.saucedemo.com/', f'Wrong URL {logout_url}'
