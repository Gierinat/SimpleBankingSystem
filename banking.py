from card import create_card


cards = []


def print_menu():
    print("""1. Create an account
2. Log into account
0. Exit"""
    )


def main_menu():
    command = ""
    while command != "0":
        print_menu()
        command = input()
        if command == "1":
            cards.append(create_card())
        elif command == "2":
            print("Logging in...")
        elif command == "0":
            print ("Bye!")


def main():
    main_menu()


if __name__ == "__main__":
    main()
