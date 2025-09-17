from db_handler import (get_card_details_by_number_pin, update_card, check_card_exists, close_card,
                        update_card_transfers)
from card_creator import Card, check_card_number


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
        elif command == "3":
            transfer(con, card)
        elif command == "4":
            close_card(con, card)
            print("The account has been closed!")
            return ""
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

    if card_details:
        print("You have successfully logged in!")
        card = create_card_obj(*card_details)
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


def transfer(con, card):
    print("""Transfer
Enter card number:""")
    transfer_to_card = input()

    if check_card_number(transfer_to_card):
        check_existence = check_card_exists(con, transfer_to_card)
        if check_existence:
            receiver_card = create_card_obj(*check_existence)
            print("Enter how much money you want to transfer:")
            amount = int(input())
            card.subtract_money(amount)
            receiver_card.add_money(amount)
            update_card_transfers(con, card, receiver_card)
        else:
            print("Such a card does not exist.")
    else:
        print("Probably you made a mistake in the card number. Please try again!")

