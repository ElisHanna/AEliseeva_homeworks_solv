import os

os.system('cls')


class BankError(Exception):
    pass


class Person:

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


class CurrencyConverter:

    def __init__(self, rates):
        self.rates = rates

    def exchange_currency(self, from_currency, amount, to_currency='BYN'):
        if from_currency not in self.rates:
            raise BankError(f'There is no such currency {from_currency}')

        if to_currency not in self.rates:
            raise BankError(f'There is no such currency {to_currency}')

        key = self.rates[from_currency]
        x = key[to_currency]
        result = round((amount * x), 2)
        return result, to_currency


class Bank:

    def __init__(self):
        self.client_id = None
        self.name = None
        self.start_balance = None
        self.years = None
        self.interest = None
        self.clients = []
        self.converter = converter

    def register_client(self, client_id, name):
        if client_id not in self.clients:
            self.client_id = client_id
            self.name = name
            self.clients.append(client_id)
        else:
            raise BankError('Client is already registered')

    def convert_currency(self, client_id, from_currency, amount, to_currency='BYN'):
        if client_id in self.clients:
            return self.converter.exchange_currency(from_currency, amount, to_currency)
        else:
            raise BankError('Client is not registered')

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id in self.clients:
            self.start_balance = start_balance
            self.years = years
        else:
            raise BankError('Client is not registered!')

    def calc_interest_rate(self, client_id):
        if client_id in self.clients:
            month = self.years*12
            counter = 0
            interest = self.start_balance
            while counter < month:
                interest += interest*(10/12)/100
                counter += 1
                self.interest = interest
            return round(interest, 2)
        else:
            raise BankError('Client is not registered!')

    def close_deposit(self, client_id):
        if client_id in self.clients:
            print(f'Client got {round(self.interest, 2)} money. Deposit is closed')
            self.start_balance = None
            self.years = None
            self.interest = None


currency_rates = {
            'BYN': {'BYN': 1.0000, 'USD': 0.3149, 'EUR': 0.2896},
            'EUR': {'BYN': 3.4530, 'USD': 1.0872, 'EUR': 1.0000},
            'USD': {'BYN': 3.1760, 'USD': 1.0000, 'EUR': 0.9198}
    }

converter = CurrencyConverter(rates=currency_rates)

vasya = Person('USD', 10)
petya = Person('EUR', 5)

print(converter.exchange_currency(vasya.currency, vasya.amount))
print(converter.exchange_currency(petya.currency, petya.amount))
print(converter.exchange_currency(vasya.currency, vasya.amount, 'EUR'))
print(converter.exchange_currency(petya.currency, petya.amount, 'USD'))

bank = Bank()

bank.register_client(client_id='00001', name='Igor')

bank.open_deposit_account(client_id='00001', start_balance=1000, years=1)
print(bank.convert_currency('00001', 'USD', 10, 'EUR'))
print(bank.convert_currency('00001', 'USD', 10,))
# bank.calc_interest_rate(client_id='00001')
# bank.close_deposit(client_id='00001')
# print(bank.clients)
