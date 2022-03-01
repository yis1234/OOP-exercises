def absences():
    # Create empty lists for names and absences
    names = []
    absences_days = []
    # Get input from user
    while True:
        name = input("Enter name of employee (enter X if you want to quit): ")\
            .title()
        if name == "X":
            break
        else:
            names.append(name)
            absences_days.append(int(input("Enter number of absences: ")))
    # Calculate average
    average = sum(absences_days) / len(absences_days)
    # Find person with most absences
    max_absences = max(absences_days)
    name_max_absences = names[absences_days.index(max_absences)]
    # Find people who were not absent
    not_absent = []
    for i in range(len(absences_days)):
        if absences_days[i] == 0:
            not_absent.append(names[i])
    # Find people with absences above average
    above_average = []
    for i in range(len(absences_days)):
        if absences_days[i] > average:
            above_average.append(names[i])
    # Print results
    print("Average number of days staff were absent:", average)
    print("Person with most days absent:", name_max_absences, "with",
          max_absences, "days absent")
    print("List of people who weren't absent at all:", *not_absent, sep="\n")
    # print people with absences above average with absences next to them
    print("People with absences above average:")
    for i in range(len(above_average)):
        print(above_average[i], ":",
              absences_days[names.index(above_average[i])])


absences()
