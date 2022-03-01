names = []
option = ""


def dropoff():
    drop_off = input("What is the name of your child? ").upper().title()
    names.append(drop_off)


def pickup():
    pick_up = input("What is the name of your child? ").upper().title()
    if pick_up in names:
        print(pick_up, "has been picked up")
        names.remove(pick_up)
    else:
        print("error")


def calc_cost():
    price_per_hour = 12
    cost = int(input("How many hours is your child going to stay for? "
                     "(please enter in numbers) "))
    print("$", cost * price_per_hour)


def print_roll():
    print(names)


while option != "5":
    option = input("========================\n"
                   "Welcome to MGS Childcare.\n"
                   "What would you like to do?\n"
                   "1. Drop off a child\n"
                   "2. Pick up a child\n"
                   "3. Calculate cost\n"
                   "4. Print roll\n"
                   "5. Exit the system\n"
                   "Enter an option from 1 to 5: ")
    if option == "1":
        dropoff()
    elif option == "2":
        pickup()
    elif option == "3":
        calc_cost()
    elif option == "4":
        print_roll()
    else:
        print("Goodbye")
        exit()
