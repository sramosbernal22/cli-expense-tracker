def add_expense(description, amount, category):
    with open("expenses.txt", "a") as file:
        file.write("Description: " + description + "\n")
        file.write("Amount: " + amount + "\n")
        file.write("Category: " + category + "\n")
        file.write("--------------------\n")

def list_expenses():
    with open("expenses.txt", "r") as file:
        content = file.read()
        print(content)

def sum_expenses():
    total = 0 
    with open("expenses.txt", "r") as file:
        for line in file:
            if line.startswith("Amount:"):
                amount = float(line.split(":")[1].strip())
                total += amount
    print(f"Total expenses: {total}")

def main():
    userInput = -1
    while userInput != 0:
        userInput = int(input("Pick following options: \n" \
        "Option 0: exit menu \n" \
        "Option 1: add expense \n" \
        "Option 2: read expenses \n" \
        "Option 3: sum expenses \n"))

        if userInput == 1:
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            add_expense(description, amount, category)
        elif userInput == 2:
            list_expenses()
        elif userInput == 3:
            sum_expenses()

main()