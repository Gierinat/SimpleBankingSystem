from card_creator import card_create
from card_actions import card_login
from db_handler import connection_maker, save_card  #, balance_all_to_zero


def print_menu():
    print("""1. Create an account
2. Log into account
0. Exit""")


def main_menu():
    # con = connection_maker()
    with connection_maker() as con:
        command = ""
        while command != "0":
            print_menu()
            command = input()
            if command == "1":
                card = card_create()
                save_card(con, card)
            if command == "2":
                command = card_login(con)
            if command == "0":
                # balance_all_to_zero(con)
                # con.close()
                print("Bye!")


def main():
    main_menu()


if __name__ == "__main__":
    main()
