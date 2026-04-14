import json
from datetime import datetime
import matplotlib.pyplot as plt

FILE = "data.json"

# Ensure file exists and is valid JSON
def init_file():
    try:
        with open(FILE, "r") as f:
            json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or contains invalid JSON, create/reset it
        with open(FILE, "w") as f:
            json.dump([], f)

# Add Expense
def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("❌ Invalid amount. Please enter a valid number.")
        return

    category = input("Enter category: ")
    note = input("Enter note: ")
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }

    with open(FILE, "r+") as file:
        data = json.load(file)
        data.append(expense)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate() # Added to prevent leftover data corruption

    print("✅ Expense added!")

# View Expenses
def view_expenses():
    with open(FILE, "r") as file:
        data = json.load(file)

    if not data:
        print("No expenses found.")
        return False # Return boolean to help delete_expense() know if it should proceed

    for i, exp in enumerate(data, 1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']} | {exp['date']}")
    
    return True

# Delete Expense
def delete_expense():
    has_data = view_expenses()
    if not has_data:
        return # Don't ask for input if there's nothing to delete

    try:
        index = int(input("Enter number to delete: ")) - 1

        with open(FILE, "r+") as file:
            data = json.load(file)

            if 0 <= index < len(data):
                removed = data.pop(index)
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                print(f"❌ Deleted: ₹{removed['amount']} ({removed['category']})")
            else:
                print("❌ Invalid index. Out of range.")
    except ValueError:
        print("❌ Please enter a valid whole number.")

# Monthly Summary
def monthly_summary():
    with open(FILE, "r") as file:
        data = json.load(file)

    if not data:
        print("No expenses to summarize.")
        return

    summary = {}

    for exp in data:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]

    print("\n📊 Summary:")
    for cat, total in summary.items():
        print(f"{cat}: ₹{total}")

    if summary:
        max_cat = max(summary, key=summary.get)
        print(f"\n💰 Highest spending: {max_cat}")

# Show Chart
def show_chart():
    with open(FILE, "r") as file:
        data = json.load(file)

    summary = {}

    for exp in data:
        summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]

    if not summary:
        print("No data to show.")
        return

    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.figure(figsize=(8, 6)) # Added figure sizing to make it look nicer
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
    plt.title("Expense Distribution")
    plt.show()

# Menu
def menu():
    init_file()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Summary")
        print("5. Show Chart")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            show_chart()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice. Please select from 1-6.")

if __name__ == "__main__":
    menu()
