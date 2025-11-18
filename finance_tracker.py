import os
import json

transactions=[]
DATA_FILE="transactions.json"

def load_transactions():
    global transactions
    if not os.path.exists(DATA_FILE):
        transactions=[]
        return()
    with open(DATA_FILE, "r") as f:
        try:
            transactions=json.load(f)
        except json.JSONDecodeError:
            transactions=[]
    
def save_transactions():
    global transactions
    with open(DATA_FILE, "w") as f:
        json.dump(transactions,f, indent=1)
    
def add_transaction():
    global transactions
    print("\n--- Add Transaction ---")
    
    try:
        amount = float(input("enter amount (positive=income, negative=expense:"))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
        
    category=input("Enter category (e.g. food, rent): ").strip()
    date=input("Enter date (YYYY-MM-DD): ").strip()
    note=input("Optional note: ").strip()
    
    transaction={
        "amount": amount,
        "category": category,
        "date": date,
        "note": note
        }
    transactions.append(transaction)
    save_transactions()
    print("Transaction added.")
    
def show_transactions():
    global transactions
    
    if not transactions:
        print("no transactions to show")
        return
    print("Showing transaction... (not implemented yet)")
    for i, t in enumerate(transactions, start=1):
        print(f"{i}. date:{t['date']}, amount: {t['amount']}, category: {t['category']}, note: {t['note']}")
    
    
def monthly_summary():
    global transactions
    print("Monthly summary... (not implemented yet)")
    
def main():
    load_transactions()
    
    while True:
        print("\n=== FINANCE TRACKER ===")
        print("1. Add transaction")
        print("2. Show all transactions")
        print("3. Monthly summary")
        print("4. Exit")
        
        choice=input("Choose: ")
        
        if choice == "1":
            add_transaction()
        elif choice =="2":
            show_transactions()
        elif choice =="3":
            monthly_summary()
        elif choice=="4":
            print("Goodbye")
            break
        else:
            print("Invalid choice, try again")
            
if __name__=="__main__":
    main()