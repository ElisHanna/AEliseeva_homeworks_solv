import os

os.system('cls')


class Card:

    number_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suit_list = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

    def __init__(self, suit, number):
        self.number = number
        self.suit = suit

    def __str__(self):
        return f'{self.suit} {self.number}'


class CardsDeck:

    def __init__(self):
        self.deck = []

    def shuffle(self):
        self.deck = ['Night Joker', 'Day Joker']
        for suit in Card.suit_list:
            for number in Card.number_list:
                self.deck.append(Card(suit, number))
        self.deck = set(self.deck)
        return self.deck

    def get(self, card_num):
        self.deck = list(self.deck)
        lenght = len(self.deck)
        if card_number not in range(1, lenght+1):
            print("Don't fool around please!")
            return None
        else:
            return self.deck[card_num-1]


deck = CardsDeck()
deck.shuffle()
card_number = int(input('Choose the card from the 54-card deck: '))
card = deck.get(card_number)
print(f'Your card is: {card}')

card_number = int(input('Choose the card from the 54-card deck: '))
card = deck.get(card_number)
print(f'Your card is: {card}')
