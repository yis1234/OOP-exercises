fine = 0
name_list = []
speed_list = []
criminal_list = ["JAMES WILSON", "HELGA NORMAN", "ZACHARY CONROY"]
fine_list = 0


def scale(speed_over_limit):
    if speed_over_limit <= 0:
        fine_ = 0
    elif speed_over_limit < 10:
        fine_ = 30
    elif 10 <= speed_over_limit <= 14:
        fine_ = 80
    elif 15 <= speed_over_limit <= 19:
        fine_ = 120
    elif 20 <= speed_over_limit <= 24:
        fine_ = 170
    elif 25 <= speed_over_limit <= 29:
        fine_ = 230
    elif 30 <= speed_over_limit <= 34:
        fine_ = 300
    elif 35 <= speed_over_limit <= 39:
        fine_ = 400
    elif 40 <= speed_over_limit <= 44:
        fine_ = 510
    else:
        fine_ = 630
    return fine_


print("===========================")
name = input("Enter name of speeder (enter X if you want to quit): ").upper()
if name == "X":
    print("Total fines:", sum(name_list))
    print("Total amount of fines:", 0)
    exit()
name_list.append(name)
for i in criminal_list:
    if name == i:
        print(name.upper(), "– WARRANT TO ARREST")
speed = (int(input("Enter the amount over speed limit: ")))
speed_list.append(speed)
print(name, "to be fined $", scale(speed))
fine_list += scale(speed)
while name != "X":
    print("===========================")
    name = input("Enter name of speeder (enter X if you want to quit): ") \
        .upper()
    if name == "X":
        break
    name_list.append(name)
    for i in criminal_list:
        if name == i:
            print(name.upper(), "– WARRANT TO ARREST")
    speed = (int(input("Enter the amount over speed limit: ")))
    speed_list.append(speed)
    print(name, "to be fined $", scale(speed))
    fine_list += scale(speed)

print("Total fines:", len(name_list))
for i in range(len(name_list)):
    print(f"{i + 1}) Name: {name_list[i]}, Amount over limit: {speed_list[i]}")
print(f"Total amount of fines: ${fine_list}")
