

capacity = float(input("Enter tank capacity: "))
level = float(input("Enter initial water level: "))
threshold = float(input("Enter threshold level: "))
days = int(input("Enter number of days: "))

overflow_count = 0
shortage_count = 0
first_threshold_day = -1

if (capacity <= 0 or level < 0 or level > capacity
        or threshold < 0 or threshold > capacity or days <= 0):

    print("Invalid tank details")

else:
    for day in range(1, days + 1):

        print("\nDay", day)

        inflow = float(input("Enter water inflow: "))
        outflow = float(input("Enter water outflow: "))

        if inflow < 0 or outflow < 0:
            print("Invalid inflow or outflow")
            continue

        new_level = level + inflow - outflow

        if new_level > capacity:
            overflow = new_level - capacity
            print("Overflow:", overflow)
            overflow_count += 1
            level = capacity

        elif new_level < 0:
            shortage = abs(new_level)
            print("Water Shortage:", shortage)
            shortage_count += 1
            level = 0

        else:
            level = new_level

        print("Current Water Level:", level)

        if level >= threshold and first_threshold_day == -1:
            first_threshold_day = day
            print("Threshold Reached on Day:", day)

    print("\n----- WATER TANK SUMMARY -----")
    print("Final Water Level:", level)
    print("Overflow Days:", overflow_count)
    print("Shortage Days:", shortage_count)

    if first_threshold_day == -1:
        print("Threshold was not reached")
    else:
        print("First Threshold Day:", first_threshold_day)

    print("Simulation Completed")

