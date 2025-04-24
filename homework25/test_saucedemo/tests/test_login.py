import pytest
from pages.login_page import LoginPage
from test_data.user_creds import UserCredentials as UC
from test_data.env import Env


def test_login(driver):
    lip = LoginPage(driver, Env.URL)
    lip.open()
    plp = lip.complete_login(UC.standard_user, UC.standard_password)
    assert plp.is_current_url(plp.url)
    assert lip.is_login_successful


@pytest.mark.xfail
def test_wrong_login(driver):
    lip = LoginPage(driver, Env.URL)
    lip.open()
    plp = lip.complete_login(UC.wrong_user, UC.standard_password)
    assert plp.is_current_url(plp.url)
    assert lip.is_login_successful
