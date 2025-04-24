from pages.login_page import LoginPage
from test_data.env import Env
from test_data.user_creds import UserCredentials as UC


def test_bying(driver):
    lip = LoginPage(driver, Env.URL)
    lip.open()
    plp = lip.complete_login(UC.standard_user, UC.standard_password)
    assert plp.is_current_url(plp.url)
    assert lip.is_login_successful
    plp.add_to_cart(6)
    plp.remove()
    cp = plp.go_to_cart()
    assert cp.is_current_url(cp.url)
    cp.remove_from_cart(4, 2)
    chop = cp.checkout()
    assert chop.is_current_url(chop.url)
    owp = chop.fill_postal_data(UC.name, UC.last_name, UC.zipcode)
    assert owp.is_current_url(owp.url)
    cmplp = owp.finish(2)
    assert cmplp.is_current_url(cmplp.url)
    hp = cmplp.go_home()
    assert hp.is_current_url(cmplp.url)
    lop = hp.logout()
    assert lop.is_current_url(lop.url)
