import manager
import transaction
import dailytotal
import os
import lane
from datetime import date


# STUFF LEFT TO DO:
  #1.) Resolving duplicate lanes
    # If same lane number, but non-overlapping times is OK
    # Same lane number and same times is not allowed
    # Same lane number and overlapping times is not allowed

    # If user enters a lane number:
      # Check if that lane number exists in transactions.txt
      # If it does, make a temporary transaction variable and temporary end time variable to retrieve its end time
    # Ask user to continue inputting lane info
      # Once it gets to the prompt that asks for lane start time, verify that the start time is not less than the lane's end time

  # [DONE]
  #2.) Use dailytotal.py file in main.py

  # [DONE]
  #3.) Various aesthetic changes
  #like if transactions.txt or lanes.txt are empty... "There are no transactions." or     "There are no lanes being used at the moment."




def empty(file): #Clay
  return os.path.getsize(file) == 0

def new_manager(): #Clay
  set_manager_name = input("Set your name: \n")
  set_password = 1
  confirm_password = 2 

  while set_password != confirm_password:
    set_password = input("Set your password: \n")
    confirm_password = input("Confirm your password: \n")
    if set_password != confirm_password:
      print("Passwords do not match. Please try again.")

  print("Your name and password have been set!")

  with open("managers.txt", "a") as file:
    file.write(f"{set_manager_name}:{set_password}\n")

  return set_manager_name, set_password


def login(): #Clay
  usernames = []
  passwords = []

  with open("managers.txt", "r") as file:
    for line in file:
      manager_name, manager_password = line.strip().split(":")
      usernames.append(manager_name)
      passwords.append(manager_password)

  while True:
    login_name = input("Username: \n")
    if login_name not in usernames:
      print("Incorrect username. Please try again.")
      continue

    menu = ""
    while True:
      login_password = input("Password: \n")
      if login_password == passwords[usernames.index(login_name)]:
        print("Login successful!")
        return login_name, login_password
      else:
        menu = int(input("Incorrect password.\n1. Try again\n2. Try different username\n3. Go back\n"))
        if menu == 1:
          continue
        elif menu == 2:
          break
        elif menu == 3:
          return None, None
    if menu == 2:
      continue
    else:
      break
  return None, None

def main():
  #Dictionary for lanes
  lanes_dict = {}
  # Define variables
  today_date = date.today().strftime("%Y-%m-%d")
  min_lane_num = 1
  max_lane_num = 30

  min_lane_cost = 10.0
  max_lane_cost = 20.0

  #Clay
  # WELCOME SCREEN
  print("Welcome to Your Bowling Alley Management System!")
  if empty("managers.txt"):
    print("It appears you dont have any current managers")
    setup = input("Would you like to set one up? (Y/N): \n")
    while True:
      if setup == "Y" or setup == "y":
        manager_name, manager_password = new_manager()
        manager1 = manager.Manager(manager_name, manager_password)
        print(f"Welcome {manager1.name_of_owner}!")
        break
      elif setup == "N" or setup == "n":
        print("Okay, have a nice day!")
        quit()
      else:
        setup = input("Invalid input. Please try again. (Y/N): \n")
  else:
    while True:
      menu1 = int(input("1: Login to Existing Account\n2. Create New account\n"))
      if menu1 == 1:
        manager_name, manager_password = login()
        if manager_name is None:
          continue
        else:
          manager1 = manager.Manager(manager_name, manager_password)
          print(f"Welcome {manager1.name_of_owner}!")
          break
      elif menu1 == 2:
        manager_name, manager_password = new_manager()
        manager1 = manager.Manager(manager_name, manager_password)
        print(f"Welcome {manager1.name_of_owner}!")
        break

  print()

  # MAIN MENU
  user_choice = 0
  while user_choice != 5:
    user_choice = int(input( "Main Menu: \n1. View all transactions \n2. View Lane Information \n3. View daily total \n4. Assign New Lane \n5. Exit\n"))

    # 1.) VIEW ALL TRANSACTIONS 
    if user_choice == 1:
        print("\nTransactions:")
        if empty("transactions.txt"):
          print("There are no transactions currently.\n")

        else:
          with open("transactions.txt", "r") as file:
            transactions = file.readlines()
            for every_transaction in transactions:
              print(every_transaction)

    # 2.) VIEW LANE INFORMATION 
    elif user_choice == 2:
        print("\nLane Information:")
        if empty("lanes.txt"):
          print("There are no lanes assigned currently.\n")

        else:
          with open("lanes.txt", "r") as file:
              lanes = file.readlines()
              for every_lane in lanes:
                print(every_lane)

    # 3.) VIEW DAILY TOTAL
    elif user_choice == 3:
        today_total = dailytotal.DailyTotal()
        today_total.set_date(today_date)

        with open("transactions.txt", "r") as file:
          transactions = file.readlines()
          daily_total = 0
          for every_transaction in transactions:
            items_in_transaction = every_transaction.strip().split("$")
            if len(items_in_transaction) == 2:
              daily_total += float(items_in_transaction[1])

          today_total.set_total(daily_total)
          print("\nDaily Total for {}:".format(today_date))
          print(f"${today_total.get_total()}0\n")

  #Josh worked on making lane and transaction print on txt file
    # 4.) ASSIGN NEW LANE
    if user_choice == 4:
        newLane = lane.Lane()

        newTransaction = transaction.Transaction()

        newLane.set_lane_number(int(input("Enter a lane number (1-30): \n")))
        while newLane.get_lane_number() < min_lane_num or newLane.get_lane_number() > max_lane_num:
          print("Invalid lane number. Please enter a number between 1 and 30.")
          new_lane_number = int(input("Enter a lane number (1-30):\n"))
          newLane.set_lane_number(new_lane_number)
          newTransaction.set_lane_number(new_lane_number)

        newTransaction.set_name(input("Enter a customer name:\n"))

        newTransaction.set_lane_start_time(int(input("Enter a start time (Please enter military time):\n")))
        while newTransaction.get_start_time() < 0 or newTransaction.get_start_time() > 24:
          print("Invalid start time. Please enter a positive integer.")
          new_start_time = int(input("Enter a start time:\n"))
          newTransaction.set_lane_start_time(new_start_time)

        newTransaction.set_lane_end_time(int(input("Enter an end time:\n")))
        while newTransaction.get_end_time() <= newTransaction.get_start_time() or newTransaction.get_end_time() > 24:
          print("Invalid end time. Please enter a time after the start time.")
          new_end_time = int(input("Enter an end time:\n"))
          newTransaction.set_lane_end_time(new_end_time)


        new_lane_cost = float(input("Enter lane cost ($10.00 - $20.00): \n"))
        while new_lane_cost < min_lane_cost or new_lane_cost > max_lane_cost:
          print("Invalid lane cost. Please enter a cost between $10.00 and $20.00.")
          new_lane_cost = float(input("Enter lane cost ($10.00 - $20.00): \n"))
        newLane.set_hourly_lane_cost(new_lane_cost)

        lane_num = newLane.get_lane_number()
        customer_name = newTransaction.get_name()
        start_time = newTransaction.get_start_time()
        end_time = newTransaction.get_end_time()
        hourly_lane_cost = newLane.get_hourly_lane_cost()
        total_cost = newLane.get_total(hourly_lane_cost, start_time, end_time)

        with open("lanes.txt", "a") as file:
          file.write(f"Lane{lane_num} - {hourly_lane_cost}\n")

        with open("transactions.txt", "a") as f:
          f.write(f"{customer_name} - Lane_{lane_num} - {today_date} - {start_time} - {end_time} - ${total_cost}\n")

    # 5.) EXIT 
    elif user_choice == 5:
        print("Exiting program...")
        file_path = 'lanes.txt'
        # Open the file in write mode, which truncates the file
        with open(file_path, 'w') as file:
            pass  # This leaves the file empty
        print("File lanes.txt has been cleaned.")

        file_path_2 = 'transactions.txt'
        # Open the file in write mode, which truncates the file
        with open(file_path_2, 'w') as file:
            pass  # This leaves the file empty
        print("File transactions.txt has been cleaned.")
        break


if __name__ == '__main__':
  main()
