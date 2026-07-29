from cli.menu import show_menu
from cli.commands import execute

def main():
    while True:
        show_menu()

        choice = input("Choose: ")

        if choice == "6":
            break

        execute(choice)

if __name__ == "__main__":
    main()
