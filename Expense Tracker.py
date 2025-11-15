import json
import os
expenses= []
def add_expense(expenses):
    p = input("What is the category of the expense: ")
    k = int(input("What is the expense: "))
    r = input("What is the date of Expense (Y/M/D): ")

    expense= {
        "date": r ,
        "amount" : k,
       "category": p,
}
    expenses.append(expense)
    print("Expenses added Successfully.")
def veiw_expenses(expenses) :
    if not expenses  :
        print("No expense Yet.")
    else:
        print("Your expenses.")
        for expense in expenses:
         print(f"Date: {expense['date']}, Category: {expense['category']}, Amount {expense['amount']}")
def total_expense(expenses):
    total = 0
    for expense in expenses:
        total = total +  expense['amount']
    print("Total Expense: ",total)
def expense_by_category(expenses):
    cat = input("Enter the Category: ")
    total_expense= 0
    found = False
    for expense in expenses:
        if expense['category'].lower() == cat.lower():
           print(f"Date: {expenses['date']}, Amount: {expense['amount']}")
           total_expense = total_expense + expense['amount'] 
           found = True
    if found:
          print("Total for this category:", total_expense)
    else:
        print("No expenses found for this category.")

def save_expenses(expenses):
    with open("expenses.json", "w") as file:   # open file in write mode
        json.dump(expenses, file, indent=4)    # convert list into JSON & save
    print("Expenses saved!")
    def load_expenses():
     if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        print("Expenses loaded successfully.")
        return expenses
     else:
        print("No saved expenses found. Starting fresh.")
        return []
while True:
    print("Expense Tracker")
    print("1.Add Expense ")
    print("2.Veiw Expenses")
    print("3.Total Expenses")
    print("4. Expenses By Catergory")
    print("5.Save and Exit")

    choice = input("Enter the Option: ")
    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        veiw_expenses(expenses)
    elif choice == "3":
        total_expense(expenses)
    elif choice == "4":
        expense_by_category(expenses)
    elif choice == "5":
        save_expenses(expenses)
    else:
        print("Invalid Choice!") 
if __name__ == "__main__":
         main()

    



