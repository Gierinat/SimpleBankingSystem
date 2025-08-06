import random as r


def generate_card_number():
    mii = "4"
    bin_num = "00000"
    can = str(r.randint(0, 999999999)).zfill(9)
    checksum = str(r.randint(0, 9))
    card_number = mii + bin_num + can + checksum
    return card_number


def generate_pin():
    pin = str(r.randint(0, 9999)).zfill(4)
    return pin


def create_card():
    card = generate_card_number()
    pin = generate_pin()
    print("Your card has been created")
    print("Your card number:")
    print(card)
    print("Your card PIN:")
    print(pin)
