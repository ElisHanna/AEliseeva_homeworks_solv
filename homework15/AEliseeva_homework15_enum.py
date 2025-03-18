import os
from enum import Enum

os.system('cls')


class OrderStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    READY = 3
    COMPLETED = 4
    CANCELLED = 5


class Order:

    def __init__(self, id):
        self.id = id
        self.status = 1

    def update_status(self, status):
        self.status = status

    def display_status(self):
        call = OrderStatus(self.status)
        print(f'Order {self.id} has status {call.name}')


first_order = Order('0001')
first_order.display_status()
first_order.update_status(3)
first_order.display_status()
