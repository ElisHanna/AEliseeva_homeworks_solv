import os
import unittest
from bank import BankError, CurrencyConverter, Bank, Person, currency_rates

os.system('cls')


class TestBank(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cust1 = Person('USD', 15)
        cls.cust2 = Person('EUR', 30)
        rates = currency_rates
        cls.conv = CurrencyConverter(rates)
        cls.bank = Bank()

    def test_exchange_currency(self):
        self.assertEqual(TestBank.conv.exchange_currency(self.cust1.currency, self.cust1.amount),
                         (47.64, 'BYN'))
        self.assertNotEqual(TestBank.conv.exchange_currency(self.cust2.currency,
                            self.cust2.amount, 'USD'), (103.59, 'BYN'))

    def test_aregister_client(self):
        self.assertIsNone(self.bank.register_client('0001', 'George'))
        self.assertIn('0001', self.bank.clients)
        with self.assertRaises(BankError) as be:
            self.bank.register_client('0001', 'George')
        self.assertEqual('Client is already registered', str(be.exception))

    def test_bopen_deposit_account(self):
        with self.assertRaises(BankError) as be:
            self.bank.open_deposit_account('0002', 5000, 2)
        self.assertNotEqual('Client is already registered', str(be.exception))
        self.assertEqual('Client is not registered!', str(be.exception))
        self.assertIn('0001', self.bank.clients)
        self.assertIsNone(TestBank.bank.open_deposit_account('0001', 1000, 3))
        self.assertRaises(TypeError, self.bank.open_deposit_account, '0002')

    def test_calc_intertest_rate(self):
        self.assertNotEqual(TestBank.bank.calc_interest_rate('0001'), 6101.95)
        self.assertEqual(TestBank.bank.calc_interest_rate('0001'), 1348.18)
        self.assertRaises(BankError, self.bank.calc_interest_rate, '0002')

    def test_cconvert_currency(self):
        self.assertEqual(TestBank.bank.convert_currency('0001', 'BYN', 10, 'EUR'),
                         (2.9, 'EUR'))
        self.assertEqual(TestBank.bank.convert_currency('0001', 'BYN', 10),
                         (10, 'BYN'))
        self.assertRaises(BankError, self.bank.convert_currency, '0002', 'USD', 50, 'EUR')
        self.assertRaises(TypeError, self.bank.convert_currency, '0002')

    def test_close_deposit(self):
        self.assertIsNone(self.bank.close_deposit('0002'))
        self.assertIn('0001', self.bank.clients)
        self.assertEqual(TestBank.bank.close_deposit('0001'),
                         f'Client got {self.bank.res} money. Deposit is closed')


if __name__ == '__main__':
    unittest.main()
