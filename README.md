﻿# EXPENSE TRACKER BUDDY
#### Video Demo:  [YouTube Video](https://youtu.be/-kjOiD1juTQ)
#### Description:
Expense tracker buddy is a python program designed to keep track of the user's expenses. The menu of the program is interactive via keyboard inputs. The interaction is text based. Here are the following features this program allows a user to do:
  1. Add new category
  2. Delete category
  3. show all expenses
  4. Reset expenses
  5. See total value of expenses
  6. Update existing category
  7. Exit expense tracker buddy

##### Files:
Inside the main folder, "project", there are four different files. Here is an overview of the project directory:
  - project (main folder)
    - "project.py" (contains all the source code)
    - "test_project.py" (test file that checks all the helping functions using pytest)
    - "requirements.txt" (lists all the dependencies)
    - README.md (the file containing the documentation and usage)

##### project.py:
This file contains all the source code that runs the program. There are 8 helper functions: 
  - set_new_category: 
  This function allows the user to input a category name and money that was spent on this. It then saves the information along with the date(using python's datetime module) inside a database using sqlite3.

  - delete_category: 
  This function asks for a existing category name and if it exists, the function deletes all the information about that particular category from the database.

  - show_all_expenses:
  This function uses the tabulate module to showcase all the expenses in a table. It gives an empty message if no rows are found.

  - reset_expenses: This function asks for  confirmation if the user really want to delete all the expenses from the database. If prompted 'yes', it will delete all the rows of the database.

  - get_total_value: 
    This function simply return the sum of all the expenses in dollars and shows $0.00 if there are no expenses

  - update_category:
  This function prompts the user to enter an existing category name and if the category is found, it prompts for money and saves the information in the database. (also updates the date using datetime module)

  - display_menu: This function simply prints out the menu containig all the instructions for the user.

  - make_database: This function creates the database and also creates the table to store all the expenses if no table is found. Later, it returns the connection to the database to the caller.

##### test_project.py:
This file creates a temporary database file to test the helper functons without altering the main database file. pytest.fixture decorator is used to achieve this. The rest of the functions check if the program stores, updates, shows, and deletes information correctly.

#### Usage:
The user will be provided with a menu full of instructions and prompted to enter a number between 1-7 or the word 'menu' to view the menu again. As per the instructions, inputtin one of the numbers will trigger the functionalities which includes adding new category, deleting category, showing all expenses, reseting expenses, showing the total value of expenses, updating an existing category, and exiting the program respectively. If the user prompts something other than the available options, the program simply reprompts the user for a valid input. If the user wants to see the menu at any point of using expense tracker buddy, they just have to type 'menu' to see it. 

##### Implementation Challenges:
Creating the test file was a bit challenging as making a demo database using the pytest.fixture was new to me. Moreover, making my helper functions pytest friendly and checking them was complex as they required to make sql queries and check if the temporary database has the required information inside it after each test.
