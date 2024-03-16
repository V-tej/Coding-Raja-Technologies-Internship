import json
import os

# Function to load transactions from file
def load_transactions():
    if os.path.exists("transactions.json"):
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
        return transactions
    else:
        return {"expenses": [], "income": []}

# Function to save transactions to file
def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

# Function to record an expense
def record_expense(transactions):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    transactions["expenses"].append({"category": category, "amount": amount})
    save_transactions(transactions)
    print("Expense recorded successfully!")

# Function to record income
def record_income(transactions):
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    transactions["income"].append({"category": category, "amount": amount})
    save_transactions(transactions)
    print("Income recorded successfully!")

# Function to calculate remaining budget
def calculate_budget(transactions):
    total_income = sum(transaction["amount"] for transaction in transactions["income"])
    total_expenses = sum(transaction["amount"] for transaction in transactions["expenses"])
    remaining_budget = total_income - total_expenses
    return remaining_budget

# Function to analyze expenses by category
def analyze_expenses(transactions):
    expenses_by_category = {}
    for transaction in transactions["expenses"]:
        category = transaction["category"]
        amount = transaction["amount"]
        if category in expenses_by_category:
            expenses_by_category[category] += amount
        else:
            expenses_by_category[category] = amount
    print("\nExpense Analysis:")
    for category, amount in expenses_by_category.items():
        print(f"{category}: ${amount}")

# Main function
def main():
    transactions = load_transactions()

    while True:
        print("\nBUDGET TRACKER MENU:")
        print("1. Record Expense")
        print("2. Record Income")
        print("3. View Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            record_expense(transactions)
        elif choice == "2":
            record_income(transactions)
        elif choice == "3":
            remaining_budget = calculate_budget(transactions)
            print(f"Remaining Budget: ${remaining_budget}")
        elif choice == "4":
            analyze_expenses(transactions)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
