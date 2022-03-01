def price():
    total_cost = 0
    total_time = 0
    passenger = 0
    base_cost = 10
    extra_cost = 2
    name = input("Please enter the name of the taxi driver: ")
    new_trip = input("Do you want to start a new trip (Y or N): ").upper()
    if new_trip == "N":
        print(name)
        exit()
    time_taken = float(input("How many minutes did the trip take: "))
    total_cost += base_cost + time_taken * extra_cost
    if time_taken > 0:
        passenger += 1
    total_time += time_taken
    while new_trip != "N":
        new_trip = input("Do you want to start a new trip (Y or N): ").upper()
        if new_trip == "N":
            print(name)
            print("Time taken for all trips is", total_time)
            print("Average time of the trips is", total_time / passenger)
            print("Total cost is $", total_cost)
            print("Average cost is $", total_cost / passenger)
            break
        time_taken = float(input("How many minutes did the trip take: "))
        total_cost += base_cost + time_taken * extra_cost
        if time_taken > 0:
            passenger += 1
        total_time += time_taken


price()




