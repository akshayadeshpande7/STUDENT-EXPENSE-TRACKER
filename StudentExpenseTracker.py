expenses = []
budget = 0


def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)

        print("Expense added successfully!")

        # Check budget after adding expense
        if budget > 0:
            total = sum(expense["amount"] for expense in expenses)

            if total > budget:
                print("ALERT! Your budget has been exceeded!")
                print(f"Exceeded Amount: ₹{total - budget}")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n===== YOUR EXPENSES =====")

    for i in range(len(expenses)):
         expense = expenses[i]

    print(f"\nExpense {i + 1}")
    print(f"Amount: ₹{expense['amount']}")
    print(f"Category: {expense['category']}")
    print(f"Description: {expense['description']}")


def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(f"{deleted['description']} deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def set_budget():
    global budget

    try:
        amount = float(input("Enter your monthly budget: ₹"))

        if amount <= 0:
            print("Budget must be greater than 0.")
            return

        budget = amount

        print(f"Budget set to ₹{budget}")

    except ValueError:
        print("Please enter a valid amount.")


def view_summary():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\n===== EXPENSE SUMMARY =====")
    print(f"Total Expenses: ₹{total}")

    if budget > 0:
        remaining = budget - total

        print(f"Budget: ₹{budget}")

        if total > budget:
            print("ALERT! Your budget has been exceeded!")
            print(f"Exceeded Amount: ₹{total - budget}")
        else:
            print(f"Remaining Budget: ₹{remaining}")

    else:
        print("Budget has not been set yet.")


def search_expense():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    keyword = input(
        "Enter category or description to search: "
    ).lower()

    found = False

    print("\n===== SEARCH RESULTS =====")

    for i, expense in enumerate(expenses, 1):


        if (keyword in expense["category"].lower()
                or keyword in expense["description"].lower()):

            print(f"\nExpense {i}")
            print(f"Amount: ₹{expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")

            found = True

    if not found:
        print("No matching expense found.")


while True:

    print("\n===== STUDENT EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Set Budget")
    print("5. View Summary")
    print("6. Search Expense")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        set_budget()

    elif choice == "5":
        view_summary()

    elif choice == "6":
        search_expense()

    elif choice == "7":
        print("Thank you for using Student Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
