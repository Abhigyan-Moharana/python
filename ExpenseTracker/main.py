import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "expenses.csv")

def add_expense(date_p,cat,amt,des):
    file_path = os.path.join(os.path.dirname(__file__), "expenses.csv")
    with open(file_path,"a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date_p,cat,amt,des])

def view_expenses():
     with open(file_path,"r") as file:
          reader = csv.reader(file)
          print("\n=== Expense Records ===")
          for i, row in enumerate(reader, start=1):
            print(f"{i}. Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")

def del_expense():
    # view_expenses()
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    
    print("\n=== Expense Records ===")
    for i, row in enumerate(rows, start=1):
        print(f"{i}. Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")

    try:
        to_delete = int(input("\nEnter the number of the entry to delete : "))
        if 1 <= to_delete <= len(rows):
            deleted_row = rows.pop(to_delete - 1)
            print(f"Deleted entry: {deleted_row}")
        else:
            print("Invalid number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    with open(file_path,"w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Expense deleted Successfully!")

def total_expense():
    total = 0

    with open(file_path,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                total += float(row[2])
            except (ValueError,IndexError):
                continue
    
    print(f"\nTotal Expense = ₹{total:.2f}")



     

while True:
    print("\n=== Personal Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete False Input")
    print("4. Calculate Total Expense")
    print("5. Exit")

    choice = int(input("Enter Choice : "))

    if choice == 1:
        print("Enter the expense details -")
        date_p = input("Date - ")
        cat = input("Category - ")
        amt = input("Amount - ")
        des = input("Description - ")
        add_expense(date_p,cat,amt,des)

    elif choice == 2:
        view_expenses()
    elif choice == 3:
        del_expense()
    elif choice == 4:
        total_expense()
    elif choice == 5:
        print("Goodbye !")
        break
    else:
        print("\n***** Invalid Input. *****")
