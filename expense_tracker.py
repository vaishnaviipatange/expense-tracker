import csv
import os

# Use relative file path for portability
FILE_PATH = os.path.join(os.path.dirname(__file__), 'expenses.csv')


def initialize_file():
    """Create CSV file if it doesn't exist."""
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Amount', 'Date'])


def add_expense():
    print("\n--- Add Expense ---")

    # Validate category
    while True:
        category = input("Enter expense category: ").strip()
        if category:
            break
        else:
            print("Category cannot be empty.")

    # Validate amount
    while True:
        amount = input("Enter expense amount: ").strip()
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")

    # Validate date
    while True:
        date = input("Enter expense date (YYYY-MM-DD): ").strip()
        parts = date.split("-")
        if len(parts) == 3 and all(parts):
            break
        else:
            print("Enter date in YYYY-MM-DD format.")

    # Write to file
    with open(FILE_PATH, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, date])
    print("Expense added successfully.")


def view_expense():
    print("\n--- All Expenses ---")
    try:
        with open(FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            data = list(reader)

            if not data:
                print("No expenses found.")
                return

            print("{:<20} {:<10} {}".format("Category", "Amount", "Date"))
            print("-" * 40)
            for row in data:
                print("{:<20} {:<10} {}".format(row[0], row[1], row[2]))

    except FileNotFoundError:
        print("Expense file not found. Please add an expense first.")


def total_expense():
    print("\n--- Total Expenses ---")
    total = 0
    try:
        with open(FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    total += float(row[1])
                except (ValueError, IndexError):
                    continue
        print("Total Expenses: ₹", total)
    except FileNotFoundError:
        print("Expense file not found.")


def category_wise_expense():
    print("\n--- Category-wise Expenses ---")
    totals = {}
    try:
        with open(FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) < 2:
                    continue
                category = row[0]
                try:
                    amount = float(row[1])
                except ValueError:
                    continue
                if category in totals:
                    totals[category] += amount
                else:
                    totals[category] = amount

        if not totals:
            print("No expenses found.")
            return

        for category, total_amount in totals.items():
            print("{:<20} ₹{}".format(category, total_amount))

    except FileNotFoundError:
        print("Expense file not found.")


def main():
    initialize_file()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expenses")
        print("4. View by Category")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            category_wise_expense()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")


if __name__ == "__main__":
    main()
