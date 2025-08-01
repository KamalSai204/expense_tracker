import pandas as pd

# Initialize or load existing expenses
try:
    expenses = pd.read_csv('sample_expenses.csv')
except FileNotFoundError:
    expenses = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    new_expense = {'Date': date, 'Category': category, 'Description': description, 'Amount': amount}
    global expenses
    expenses = pd.concat([expenses, pd.DataFrame([new_expense])], ignore_index=True)
    expenses.to_csv('sample_expenses.csv', index=False)
    print("Expense added!")

def view_summary():
    if expenses.empty:
        print("No expenses recorded yet.")
        return
    print("\nTotal spent: ₹{:.2f}".format(expenses['Amount'].sum()))
    print("\nSpending by category:")
    print(expenses.groupby('Category')['Amount'].sum())
    print("\nRecent expenses:")
    print(expenses.sort_values(by='Date', ascending=False).head(5)[['Date', 'Category', 'Description', 'Amount']])

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add expense")
        print("2. View summary")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

main()