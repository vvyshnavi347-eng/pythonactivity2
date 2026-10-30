

attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes conducted: "))
threshold = float(input("Enter eligibility percentage: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details")

else:
    current = (attended / total) * 100

    print("\nCurrent Attendance:", round(current, 2), "%")

    n = int(input("Enter number of future scenarios: "))

    for i in range(n):
        print("\nScenario", i + 1)

        future_attend = int(input("Enter future classes to attend: "))
        future_miss = int(input("Enter future classes to miss: "))

        if future_attend < 0 or future_miss < 0:
            print("Invalid future class details")
            continue

        new_attended = attended + future_attend
        new_total = total + future_attend + future_miss

        percentage = (new_attended / new_total) * 100

        print("Attendance after scenario:",
              round(percentage, 2), "%")

        extra = 0

        while ((new_attended + extra) /
               (new_total + extra)) * 100 < threshold:
            extra += 1

        if extra == 0:
            print("Already eligible!")
        else:
            print("Minimum consecutive classes required:", extra)

        final_percentage = (
            (new_attended + extra) / (new_total + extra)
        ) * 100

        print("Final attendance percentage:",
              round(final_percentage, 2), "%")

print("\nProgram Completed")
