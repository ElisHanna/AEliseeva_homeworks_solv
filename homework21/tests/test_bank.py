import pytest
import logging
from apps.bank import BankError, Person, CurrencyConverter, Bank, currency_rates


logger = logging.getLogger()
file = logging.FileHandler('test_bank_pytest.log')
file.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(file)
logger.setLevel(logging.DEBUG)


@pytest.fixture
def cust_one():
    return Person('USD', 15)


@pytest.fixture
def cust_two():
    return Person('EUR', 30)


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def converter():
    return CurrencyConverter(currency_rates)


def test_exchange_currency(converter, cust_one, cust_two):
    assert converter.exchange_currency(cust_one.currency, cust_one.amount) == (47.64, 'BYN')
    assert converter.exchange_currency(cust_two.currency, cust_one.amount, 'USD') != \
           (103.59, 'BYN')
    logger.info('Test test_exchange_currency passed')


def test_register_client(bank):
    assert bank.register_client('0001', 'George') is None
    assert bank.client_id in bank.clients
    with pytest.raises(BankError) as excinfo:
        bank.register_client('0001', 'George')
        assert 'Client is already registered' in str(excinfo.value)
    logger.info('Test test_register_client passed')


def test_open_deposit_account(bank):
    bank.clients = ['0001']
    assert bank.open_deposit_account('0001', 1000, 3) is None
    with pytest.raises(BankError) as excinfo:
        bank.open_deposit_account('0002', 5000, 2)
        assert 'Client is not registered!' in str(excinfo.value)
    with pytest.raises(TypeError) as exc:
        bank.open_deposit_account('0002')
        assert exc is True
    logger.info('Test test_open_deposit_account passed')


def test_convert_currency(bank):
    bank.clients = ['0001']
    assert bank.convert_currency('0001', 'BYN', 10, 'EUR') == (2.9, 'EUR')
    assert bank.convert_currency('0001', 'BYN', 10) == (10, 'BYN')
    with pytest.raises(BankError) as excinfo:
        bank.convert_currency('0002', 'USD', 50, 'EUR')
        assert 'Client is not registered!' in str(excinfo.value)
    logger.info('Test test_convert_currency passed')


def test_calc_interest_rate(bank):
    bank.register_client('0001', 'George')
    bank.open_deposit_account('0001', 1000, 3)
    assert bank.calc_interest_rate('0001') == 1348.18
    logger.info('Test test_calc_interest_rate passed')


def test_close_deposit(bank):
    bank.register_client('0001', 'George')
    bank.open_deposit_account('0001', 1000, 3)
    bank.calc_interest_rate('0001')
    assert bank.close_deposit('0001') == f'Client got {bank.res} money. Deposit is closed'
    assert bank.close_deposit('0002') is None
    logger.info('Test test_close_deposit passed')
