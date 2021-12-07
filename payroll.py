
import random
import time
import datetime



class Employee():
    def __init__(self, name, age, position, pay):
        self.name = name
        self.age = age
        self.position = position
        self.pay = pay

class Timecard():
    def __init__(self, clock_in, clock_out, submitted_at):
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.submitted_at = submitted_at

class PTORequest():
    def __init__(self, first_day, last_day, requested_at):
        self.first_day = first_day
        self.last_day = last_day
        self.requested_at = requested_at

class 


def new_timecard():
    print("WARNING: Time must be entered in 24 hour format")
    # Clock in on timecard
    clock_in = input("Enter start time in hours:min format: ")
    # Clock out on timecard
    clock_out = input("Enter end time in hours:min format: ")
    # Submit timecard
    submitted_at = input("Do you want to submit this time card? (y/n): ")
    # Edit timecard
    user = Timecard(clock_in, clock_out, submitted_at)

# def list_employees():
#   name =
#
# def new_employee():
#
#
# def pto_request():



print("Welcome. Choose from the following menu of options: 1) See all employees, 2) New Employee, 3) New Timecard, 4) PTO Request")

choice = input("What do you want to do? > ")
if choice == 1:
    list_employees()
elif choice == 2:
    new_employee()
elif choice == 3:
    new_timecard()
elif choice == 4:
    pto_request()
