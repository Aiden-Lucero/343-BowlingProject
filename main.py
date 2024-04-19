import manager
import transaction
from lane import Lane
import dailytotal
import os
import lane
from datetime import date

# constant
min_lane_num = 1
max_lane_num = 30

min_lane_cost = 10.0
max_lane_cost = 20.0

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
  import lane
  from datetime import date
  #Dictionary for lanes
  lanes_dict = {}
  # Define variables
  min_lane_num = 1
  max_lane_num = 30

  min_lane_cost = 10.0
  max_lane_cost = 20.0

  #Clay
  print("Welcome to Your Bowling Alley Management System!")
  if empty("managers.txt"):
    print("It appears you dont have any current managers")
    setup = input("Woudld you like to set one up? (Y/N): \n")
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
  
  #Create a main_menu 
  # Define variables
  user_choice = 0
  while user_choice != 5:
    user_choice = int(input( "Main Menu: \n1. View all transactions \n2. View Lane Information \n3. View daily total \n4. Assign New Lane \n5. Exit\n"))
    if user_choice == 1:
        with open("transactions.txt", "r") as file:
          transactions = file.readlines()
          for transaction in transactions:
            print(transaction)
  
    elif user_choice == 2:
        with open("lanes.txt", "r") as file:
          lanes = file.readlines()
          for lane in lanes:
            print(lane)
  
    elif user_choice == 3:
        with open("transactions.txt", "r") as file:
          transactions = file.readlines()
          daily_total = 0
          for transaction in transactions:
            items_in_transaction = transaction.strip().split("$")
            if len(items_in_transaction) == 2:
              daily_total += float(items_in_transaction[1])
            #start_time = float(items_in_transaction[-2])
            #end_time = float(items_in_transaction[-1])
            #total_time = end_time - start_time
            #aiden added this trying to fix transaction
            #if items_in_transaction[1] in lanes_dict:
              #cost_of_lane = lanes_dict[items_in_transaction[1]]
              #daily_total += total_time * cost_of_lane
          print(daily_total)
            
  #Josh worked on making lane and transaction print on txt file
    if user_choice == 4:
        newLane = lane.Lane()
        
        newLane.set_lane_number(int(input("Enter a lane number (1-30): \n")))
        while newLane.get_lane_number() < min_lane_num or newLane.get_lane_number() > max_lane_num:
          print("Invalid lane number. Please enter a number between 1 and 30.")
          new_lane_number = int(input("Enter a lane number (1-30):\n"))
          newLane.set_lane_number(new_lane_number)
  
        newLane.set_cutomer_name(input("Enter a customer name:\n"))
  
        newLane.set_start_time(int(input("Enter a start time(Please enter military time):\n")))
        while newLane.get_start_time() < 0 or newLane.get_start_time() > 24:
          print("Invalid start time. Please enter a positive integer.")
          new_start_time = int(input("Enter a start time:\n"))
          newLane.set_start_time(new_start_time)
  
        newLane.set_end_time(int(input("Enter an end time:\n")))
        while newLane.get_end_time() < newLane.get_start_time() or newLane.get_end_time() > 24:
          print("Invalid end time. Please enter a time after the start time.")
          new_end_time = int(input("Enter an end time:\n"))
          newLane.set_end_time(new_end_time)
  
  
        new_lane_cost = float(input("Enter lane cost ($10.00 - $20.00): \n"))
        while new_lane_cost < min_lane_cost or new_lane_cost > max_lane_cost:
          print("Invalid lane cost. Please enter a cost between $10.00 and $20.00.")
          new_lane_cost = float(input("Enter lane cost ($10.00 - $20.00): \n"))
        newLane.set_hourly_lane_cost(new_lane_cost)
  
        lane_num = newLane.get_lane_number()
        customer_name = newLane.get_customer_name()
        today_date = date.today().strftime("%Y-%m-%d")
        start_time = newLane.get_start_time()
        end_time = newLane.get_end_time()
        hourly_lane_cost = newLane.get_hourly_lane_cost()
        total_cost = newLane.get_total(hourly_lane_cost, start_time, end_time)
        
        with open("lanes.txt", "a") as file:
          file.write(f"Lane{lane_num} - {hourly_lane_cost}\n")
  
        with open("transactions.txt", "a") as f:
          f.write(f"{customer_name} - Lane_{lane_num} - {today_date} - {start_time} - {end_time} - ${total_cost}\n")
  
    elif user_choice == 5:
        print("Exiting program...")
        file_path = 'lanes.txt'
        # Open the file in write mode, which truncates the file
        with open(file_path, 'w') as file:
            pass  # This leaves the file empty
        print("File lanes.txt has been cleaned.")
        break
  

if __name__ == '__main__':
  main()
