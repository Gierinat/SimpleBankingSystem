from db_handler import get_card_details_by_number_pin
from db_handler import update_card
from card_creator import Card


def print_menu():
    print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")


def create_card_obj(number, pin, bal):
    return Card(number, pin, bal)


def card_operations(con, card):
    command = "x"
    while command not in "05":
        print_menu()
        command = input()
        if command == "1":
            bal = card.balance
            print("Balance:", bal)
        elif command == "2":
            add_income(con, card)
        elif command == "5":
            print("You have successfully logged out!")
            return ""
        else:
            return "0"


def card_login(con):
    operation = ""
    print("Enter your card number:")
    card_number = input()
    print("Enter your PIN:")
    card_pin = input()

    card_details = get_card_details_by_number_pin(con, card_number, card_pin)
    card = create_card_obj(*card_details)
    if card:
        print("You have successfully logged in!")
        operation = card_operations(con, card)
    else:
        print("Wrong card number or PIN!")

    return operation


def add_income(con, card):
    print("Enter income:")
    income = int(input())

    card.add_money(income)
    update_card(con, card)

    print("Income was added!")
