import os

os.system('cls')


class BankError(Exception):
    pass


class Bank:

    def __init__(self):
        self.client_id = None
        self.name = None
        self.start_balance = None
        self.years = None
        self.interest = None
        self.clients = []

    def register_client(self, client_id, name):
        if client_id not in self.clients:
            self.client_id = client_id
            self.name = name
            self.clients.append(client_id)
        else:
            raise BankError('Client is already registered')

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


# client_id = '00001'

bank = Bank()

bank.register_client(client_id='00001', name='Igor')
bank.open_deposit_account(client_id='00001', start_balance=1000, years=1)
bank.calc_interest_rate(client_id='00001')
bank.close_deposit(client_id='00001')
print(bank.clients)
