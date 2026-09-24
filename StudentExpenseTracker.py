# Store all expenses here
expenses = []

# Store the monthly budget
budget = 0


# Function to add a new expense
def add_expense():
    try:
        # Take amount from user
        amount = float(input("Enter amount: ₹"))

        # Amount should be greater than 0
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        # Take category and description
        category = input("Enter category: ")
        description = input("Enter description: ")

        # Store expense details
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        # Add expense to the list
        expenses.append(expense)

        print("Expense added successfully!")

        # Check if budget is set
        if budget > 0:
            # Find total expenses
            total = sum(expense["amount"] for expense in expenses)

            # Check if budget is crossed
            if total > budget:
                print("ALERT! Your budget has been exceeded!")
                print(f"Exceeded Amount: ₹{total - budget}")

    # Handle wrong amount input
    except ValueError:
        print("Please enter a valid amount.")


# Function to display expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n===== YOUR EXPENSES =====")

    # Go through the expenses list
    for i in range(len(expenses)):
         expense = expenses[i]

    # Print expense details
    print(f"\nExpense {i + 1}")
    print(f"Amount: ₹{expense['amount']}")
    print(f"Category: {expense['category']}")
    print(f"Description: {expense['description']}")


# Function to delete an expense
def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    # Show expenses before deleting
    view_expenses()

    try:
        # Ask which expense to delete
        number = int(input("\nEnter expense number to delete: "))

        # Check if the number is valid
        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            print(f"{deleted['description']} deleted successfully!")
        else:
            print("Invalid expense number.")

    # Handle wrong input
    except ValueError:
        print("Please enter a valid number.")


# Function to set the budget
def set_budget():
    global budget

    try:
        # Take monthly budget from user
        amount = float(input("Enter your monthly budget: ₹"))

        if amount <= 0:
            print("Budget must be greater than 0.")
            return

        # Save the budget
        budget = amount

        print(f"Budget set to ₹{budget}")

    # Handle invalid input
    except ValueError:
        print("Please enter a valid amount.")


# Function to show total expense and budget details
def view_summary():
    total = 0

    # Add all expense amounts
    for expense in expenses:
        total += expense["amount"]

    print("\n===== EXPENSE SUMMARY =====")
    print(f"Total Expenses: ₹{total}")

    # Show budget details if budget is set
    if budget > 0:
        remaining = budget - total

        print(f"Budget: ₹{budget}")

        # Check if expenses are more than budget
        if total > budget:
            print("ALERT! Your budget has been exceeded!")
            print(f"Exceeded Amount: ₹{total - budget}")
        else:
            print(f"Remaining Budget: ₹{remaining}")

    else:
        print("Budget has not been set yet.")


# Function to search for an expense
def search_expense():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    # Take search word from user
    keyword = input(
        "Enter category or description to search: "
    ).lower()

    # Used to check if any expense is found
    found = False

    print("\n===== SEARCH RESULTS =====")

    # Check each expense one by one
    for i, expense in enumerate(expenses, 1):

        # Search in category or description
        if (keyword in expense["category"].lower()
                or keyword in expense["description"].lower()):

            print(f"\nExpense {i}")
            print(f"Amount: ₹{expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")

            # Matching expense found
            found = True

    # Show message if nothing matched
    if not found:
        print("No matching expense found.")


# Keep showing the menu until user exits
while True:

    print("\n===== STUDENT EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Set Budget")
    print("5. View Summary")
    print("6. Search Expense")
    print("7. Exit")

    # Ask user to choose an option
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
```
