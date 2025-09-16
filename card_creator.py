import random as r


class Card:
    def __init__(self, number=None, pin=None, bal=None):
        self.card_number = number if number else generate_card_number()
        self.pin = pin if pin else generate_pin()
        self.balance = bal if bal else 0

    def add_money(self, money):
        if money > 0:
            self.balance += money
        else:
            print("Wrong amount.")


# Luhn Algorithm implementation
# https://hyperskill.org/projects/109/stages/592/implement
def generate_checksum(card_number):
    odd_nums_double = [int(n) * 2 for n in card_number[0::2]]
    odd_clean = list(map(lambda x: x - 9 if x > 9 else x, odd_nums_double))
    even_nums = [int(n) for n in card_number[1::2]]
    sum_of_all = sum(odd_clean + even_nums)

    checksum = 0
    for _ in range(10):
        if sum_of_all % 10 == 0:
            break
        else:
            checksum += 1
            sum_of_all += 1

    return str(checksum)


def generate_card_number():
    mii = "4"
    bin_num = "00000"
    can = str(r.randint(0, 999999999)).zfill(9)
    card_number = mii + bin_num + can
    checksum = generate_checksum(card_number)
    card_number = card_number + checksum
    return card_number


def generate_pin():
    pin = str(r.randint(0, 9999)).zfill(4)
    return pin


def card_create():
    card = Card()

    print("Your card has been created")
    print("Your card number:")
    print(card.card_number)
    print("Your card PIN:")
    print(card.pin)
    return card
