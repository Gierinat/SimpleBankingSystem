def print_menu():
    print("""1. Balance
2. Log out
0. Exit"""
          )


def card_operations():
    command = "x"
    while command not in "02":
        print_menu()
        command = input()
        if command == "1":
            print("Balance: 0")
        else:
            print("You have successfully logged out!")
            break


def card_login(cards):
    print("Enter your card number:")
    card_number = input()
    print("Enter your PIN:")
    card_pin = input()

    for card in cards:
        if card.card_number == card_number and card.pin == card_pin:
            print("You have successfully logged in!")
            card_operations()
        else:
            print("Wrong card number or PIN!")
