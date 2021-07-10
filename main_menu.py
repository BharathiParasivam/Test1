"""
This module contains the main menu which needs to be executed as below
    python3.8 main_menu.py 09:00 12:00
argv[0] - name of python module (main_menu.py)
argv[1] - start time for customer booking vehicle (09:00)
argv[2] - end time for customer booking vehicle (12:00)
"""
import sys
import datetime

from vehicle import Vehicle
from inventory import Inventory
from logger import  Logger

# Getting logger object
logger = Logger()
logger = logger.get_logger_object()

# Getting Inventory object
inventory = Inventory(logger)


def time_in_range(start, end, current):
    """
    Check current time exist between given time slot
    :param start: start time for customer booking vehicle (datetime object)
    :param end: end time for customer booking vehicle (datetime object)
    :param current: current time of customer booking vehicle (datetime object)
    :return: True : if current time exist between start and end time
             False: if current time doesn't exist between start and end time
    """
    return start <= current <= end

def main_menu():
    """
    Provisioning of login option for customer and Manager
    """
    while True:
        print('\n*********** Welcome to ABC Vehicle Inventory Management System ***********\n')
        print('#1 For Manager Login')
        print('#2 For Customer Login')
        print('#3 Quit\n')
        user_input = input('Please choose from one of the above options: ')
        if user_input == "1":
            manager_operation()
        elif user_input == "2":
            customer_operation()
        elif user_input == "3":
            print('\n*********** Thanks for visiting ABC Vehicle Inventory Management System ***********\n')
            return
        else:
            print("Enter a valid option!!!")

def customer_operation():
    """
    Provisioning for customer relevant operations
    """
    while True:
        current_time = datetime.datetime.now().time()
        if time_in_range(start_time, end_time, current_time):
            logger.info("Logged in as Customer...")
            print("\nContinue with Customer Login...")
            print('#1 Book Vehicle to Inventory')
            print('#2 Log-out\n')
            user_input = input('Please choose from one of the above options: ')
            print('\n')
            if user_input == "1":
                logger.info("Customer wishes to book Vehicle...")
                print("\nContinue with Customer Login...")
                inventory.book_vehicle()
            elif user_input == "2":
                logger.info("Customer logged out")
                print("Back to Main Menu...")
                return
            else:
                logger.error("Wrong option selected by customer")
                print("Enter a valid option!!!")
        else:
            logger.error("\nCustomer are only allowed to access portal within timeslot of {} and {}".format(start.strftime("%H:%M"), end.strftime("%H:%M")))
            print("\nCustomer are only allowed to access portal within timeslot of {} and {}".format(start.strftime("%H:%M"), end.strftime("%H:%M")))
            return

def manager_operation():
    """
    Provisioning for Manager relevant operations
    """
    while True:
        logger.info("Logged in as Manager...")
        print("\nContinue with Manager Login...")
        print('#1 Add Vehicle to Inventory')
        print('#2 View Current Inventory')
        print('#3 Delete Vehicle from Inventory')
        print('#4 Update Vehicle in Inventory')
        print('#5 Log-out\n')
        user_input = input('Please choose from one of the above options: ')
        print('\n')
        if user_input == "1":
            logger.info("Manager choose to add vehicle record")
            inventory.add_vehicle()
        elif user_input == "2":
            logger.info("Manager choose to view vehicle records")
            inventory.view_vehicles()
        elif user_input == "3":
            logger.info("Manager choose to delete vehicle record")
            inventory.delete_vehicle()
        elif user_input == "4":
            logger.info("Manager choose to update vehicle record")
            inventory.update_vehicle()
        elif user_input == "5":
            logger.info("Manager logged out")
            print("Back to Main Menu...")
            return
        else:
            logger.error("Wrong option selected by Manager")
            print("Enter a valid option!!!")

if __name__ == "__main__":
    """
    Main function
    """
    try:
        start_time = sys.argv[1]
        end_time = sys.argv[2]
        logger.debug("Start time {} and End time {} passed as arguments".format(start_time, end_time))
    except IndexError:
        logger.error("Please pass customer timeslot as argument in 24hr format\nExample: 11:00 13:00\npython3.8 main_menu.py 09:00 14:00")
        print("Please pass customer timeslot as argument in 24hr format\nExample: 11:00 13:00\npython3.8 main_menu.py 09:00 14:00")
        sys.exit(1)
    try:
        start_time = start_time.split(':')
        end_time = end_time.split(':')
        start_time = datetime.time(int(start_time[0]), int(start_time[1]), 0)
        end_time = datetime.time(int(end_time[0]), int(end_time[1]), 0)
        logger.debug("Timeslot for customer {} and {}".format(start_time, end_time))
    except Exception as e:
        logger.error("Customer Timeslot argument is not valid :: {}".format(e))
        print("Pass customer timeslot as argument in valid 24hr format\nExample: 11:00 13:00")
        sys.exit(1)
    main_menu()
