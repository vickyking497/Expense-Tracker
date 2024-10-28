# Expense Tracker Program

import json
from datetime import datetime

# Function to load expenses from a file
def load_expenses(filename):
    """Load expenses from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save expenses to a file
def save_expenses(expenses, filename):
    """Save expenses to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(expenses, file)

# Function to add an expense
def add_expense(expenses):
    """Prompt user to add an expense."""
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category (e.g., food, transportation, entertainment): ")

        expense = {
            "amount": amount,
            "description": description,
            "category": category,
            "date": datetime.now().isoformat()
        }
        expenses.append(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")

# Function to display monthly summary
def display_summary(expenses):
    """Display a summary of expenses by category and total spent."""
    if not expenses:
        print("No expenses recorded.")
        return

    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total_spent:.2f}")

    category_summary = {}
    for expense in expenses:
        category = expense['category']
        category_summary[category] = category_summary.get(category, 0) + expense['amount']

    print("\nExpenses by Category:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")

def main():
    """Main function to run the Expense Tracker program."""
    filename = 'expenses.json'
    expenses = load_expenses(filename)

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses, filename)
        elif choice == '2':
            display_summary(expenses)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()