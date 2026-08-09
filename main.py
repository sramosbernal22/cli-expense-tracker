FILE_PATH = "expenses.txt"


def open_expense_file(mode="r"):
    try:
        return open(FILE_PATH, mode)
    except FileNotFoundError:
        if mode.startswith("r"):
            print(f"Expense file not found: {FILE_PATH}. A new file will be created when you add an expense.")
            return None
        raise
    except OSError as error:
        print(f"Unable to open '{FILE_PATH}': {error}")
        return None


def add_expense(description, amount, category):
    file = open_expense_file("a")
    if file is None:
        return

    with file:
        file.write(f"Description: {description}\n")
        file.write(f"Amount: {amount}\n")
        file.write(f"Category: {category}\n")
        file.write("--------------------\n")

    print("Expense added.")


def read_expense_file():
    file = open_expense_file("r")
    if file is None:
        return []

    with file:
        return file.readlines()


def list_expenses():
    lines = read_expense_file()
    if not lines:
        print("No expenses to show.")
        return

    print("".join(lines))


def parse_amount_line(line):
    try:
        _, value = line.split(":", 1)
        return float(value.strip())
    except (ValueError, IndexError):
        print(f"Skipping corrupt amount line: {line.strip()}")
        return None


def sum_expenses():
    total = 0.0
    lines = read_expense_file()
    if not lines:
        print("No expenses to sum.")
        return

    for line in lines:
        if line.startswith("Amount:"):
            amount = parse_amount_line(line)
            if amount is not None:
                total += amount

    print(f"Total expenses: {total}")


def get_amount_input():
    while True:
        amount_text = input("Enter amount: ")
        try:
            if float(amount_text) <= 0:
                print("Amount must be greater than zero.")
                continue
            return float(amount_text)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")


def get_menu_choice():
    try:
        return int(input("Pick following options:\n"
                         "Option 0: exit menu\n"
                         "Option 1: add expense\n"
                         "Option 2: read expenses\n"
                         "Option 3: sum expenses\n"))
    except ValueError:
        print("Invalid input. Enter a number from 0 to 3.")
        return None


def main():
    while True:
        user_input = get_menu_choice()
        if user_input is None:
            continue

        if user_input == 0:
            break
        elif user_input == 1:
            description = input("Enter description: ")
            amount = get_amount_input()
            category = input("Enter category: ")
            add_expense(description, amount, category)
        elif user_input == 2:
            list_expenses()
        elif user_input == 3:
            sum_expenses()
        else:
            print("Invalid option. Please try again.")

    print("Goodbye.")


main()
