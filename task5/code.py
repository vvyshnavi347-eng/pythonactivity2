

print("SMART PARKING FEE MANAGEMENT")

vehicle = input("Enter vehicle category (bike/car/bus): ").lower()

entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")

try:
    eh, em = map(int, entry.split(":"))
    xh, xm = map(int, exit_time.split(":"))

    if not (0 <= eh <= 23 and 0 <= xh <= 23
            and 0 <= em <= 59 and 0 <= xm <= 59):
        print("Invalid time input")

    elif vehicle not in ["bike", "car", "bus"]:
        print("Invalid vehicle category")

    else:
        entry_minutes = eh * 60 + em
        exit_minutes = xh * 60 + xm

        if exit_minutes < entry_minutes:
            duration = (24 * 60 - entry_minutes) + exit_minutes
        else:
            duration = exit_minutes - entry_minutes

        hours = (duration + 59) // 60

        rates = {
            "bike": 10,
            "car": 20,
            "bus": 40
        }

        rate = rates[vehicle]

        days = max(1, (duration + 1439) // 1440)
        daily_fee = min(hours * rate, 200 * days)

        penalty = 50 if duration > 1440 else 0

        total_fee = daily_fee + penalty

        print("\n----- PARKING BILL -----")
        print("Vehicle Category:", vehicle)
        print("Parking Duration:", duration // 60,
              "hours", duration % 60, "minutes")
        print("Total Charge: Rs.", daily_fee)
        print("Penalty: Rs.", penalty)
        print("Final Parking Fee: Rs.", total_fee)

except ValueError:
    print("Invalid time format. Use HH:MM.")

