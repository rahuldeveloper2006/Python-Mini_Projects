# now we make a expense tracker by importing CSV module
import csv
import csv

file_name = "expense_track.csv"

# Add Expense
def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category])

    print("Expense added successfully")


# View Expense
def show_expense():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)

            print("\nExpense List :")
            expenses = [row for row in reader if row]   # remove empty rows

            for i, row in enumerate(expenses):
                print(i, row)

    except:
        print("No data found")


# Delete Specific Expense
def delete_expense():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            expenses = [row for row in reader if row]

        for i, row in enumerate(expenses):
            print(i, row)

        index = int(input("Enter expense number to delete: "))

        expenses.pop(index)

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(expenses)

        print("Expense deleted successfully")

    except:
        print("Error deleting expense")


# Delete All Expense
def delete_all():
    open(file_name, "w").close()
    print("All expenses deleted")


# Total Expense
def total_expense():
    total = 0
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    total += float(row[1])

        print("Total Expense :", total)

    except:
        print("No data found")


# Main Menu
while True:

    print("\n----------- Expense Tracker -----------")
    print("1. Add expense")
    print("2. View expense")
    print("3. Delete specific expense")
    print("4. Delete all expense")
    print("5. Total expenses")
    print("6. Exit")

    choice = input("Enter choice : ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expense()

    elif choice == "3":
        delete_expense()

    elif choice == "4":
        delete_all()

    elif choice == "5":
        total_expense()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice")


