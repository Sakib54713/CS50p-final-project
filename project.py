import sqlite3
from tabulate import tabulate
from datetime import date


def main():
    con = make_database()
    cur = con.cursor()

    display_menu()
    
    while True:
        choice = input("Enter one option from (1-7) or type \"menu\" to display menu: ").strip().lower()

        if choice == "1":
            try:
                category = input("Enter the name of a new category: ").strip().lower()
                
        
                money = float(input("Money: "))

                dated = date.today().strftime("%Y-%m-%d")

                print(set_new_category(con, cur, category, money, dated))
            except ValueError:
                print("money must be a float or integer")

        elif choice == "2":
            category = input("Enter the category name you want to delete: ").strip().lower()
            print(delete_category(con, cur, category))

        elif choice == "3":
            show_all_expenses(cur)

        elif choice == "4":
            print("Do you really want to delete all the existing categories?")
            choice = input("Type \"yes\" or \"no\": ").strip().lower()

            print(reset_expenses(con, cur, choice))

        elif choice == "5":
            print(get_total_value(cur))

        elif choice == "6":
            try:
                category = input("Enter the name of your existing category: ")
                money = float(input("Updated amount of money: "))

                dated  = date.today().strftime("%Y-%m-%d")

                print(update_category(con, cur, money, dated, category))

            except ValueError:
                return f"Money must be a float or integer"
            
        elif choice == "7":
            print("Exiting your expense tracker buddy...")
            break
        elif choice == "menu":
            display_menu()
        else:
            print("Invalid input, please try (1-7) or \'menu\'")

    cur.close()
    con.close()


def set_new_category(con, cur, category, money, dated):
    try:
        if not category:
                    return "Category name cannot be empty."
        
        cur.execute("INSERT INTO expenses (category, money, date) VALUES(?, ?, ?)", (category, money, dated))

        con.commit()

        return f"{category} was added successfully with amount ${money:.2f}"

    except sqlite3.Error:
        return f"Couldn't set new category, please try again..."


def delete_category(con, cur, category):
    try:
        cur.execute("DELETE FROM expenses WHERE category = ?", (category,))
        con.commit()

        if cur.rowcount == 0:
            return f"No category named '{category}' found, no category was deleted"

        return f"{category} was successfully deleted."
    
    except sqlite3.Error:
        return f"Couldn't delete category, please try again..."


def show_all_expenses(cur):
    try:
        cur.execute("SELECT * FROM expenses")

        rows = cur.fetchall()

        if not rows:
            print("Your expense tracker buddy is empty")
        else:
            headers = ["Id", "Category", "Amount ($)", "Date"]

            print(tabulate(rows, headers, tablefmt="pretty"))

    except sqlite3.Error:
        print(f"An issue occured while getting your expenses, please try again...")


def reset_expenses(con, cur, choice):
    while True:

        if choice == "yes":
            try:
                cur.execute("DELETE FROM expenses")
                cur.execute("DELETE FROM sqlite_sequence WHERE name='expenses'")

                con.commit()

                return f"Your expenses tracker buddy has been successfully reset"
            
            except sqlite3.Error as e:
                return f"An issue occured while reseting your expense tracker buddy, please try again..."
            
        elif choice == "no":
            return f"Your expenses tracker buddy was not reset"
        else:
            return "Invalid input. Please try again."


def get_total_value(cur):
    try:
        cur.execute("SELECT SUM(money) FROM expenses")

        total = cur.fetchone()[0]

        if total is None:
            return f"Total: $0.00"
        else:
            return f"Total: ${total:.2f}"
        
    except sqlite3.Error:
        return f"An issue occured while getting your total expenses, please try again..."


def update_category(con, cur, money, dated, category):
    try:
        cur.execute("UPDATE expenses SET money = ?, date = ? WHERE category = ?", (money, dated, category))
        con.commit()

        if cur.rowcount == 0:
            return f"No category named '{category}' found, no updates made."

        return f"{category} was updated with amount ${money:.2f}"
    
    except sqlite3.Error:
        return f"An issue occured while updating the category, please try again..."
    

def display_menu():
    print("""
Welcome to your expense tracker buddy!
Expense tracker menu:
    1. Add new category
    2. Delete category
    3. show all expenses
    4. Reset expenses
    5. See total value of expenses
    6. Update existing category
    7. Exit expense tracker buddy
          """)



def make_database():
    con = sqlite3.connect("expenses.db")
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL UNIQUE, 
                money REAL NOT NULL,
                date TEXT NOT NULL)
               """)
    
    con.commit()
    
    return con


if __name__ == "__main__":
    main()
