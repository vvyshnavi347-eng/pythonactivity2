

distance = float(input("Enter journey distance (km): "))
reserve = float(input("Enter reserve fuel percentage: "))
n = int(input("Enter number of vehicles: "))

best_cost = float('inf')
best_vehicle = ""

for i in range(n):
    print("\nEnter details of Vehicle", i + 1)

    name = input("Enter vehicle name: ")
    mileage = float(input("Enter mileage (km/litre): "))
    price = float(input("Enter fuel price per litre: "))
    capacity = float(input("Enter fuel tank capacity (litres): "))

    if mileage <= 0 or price < 0 or capacity < 0:
        print("Invalid vehicle details")
        continue

    fuel = distance / mileage

    reserve_fuel = fuel * reserve / 100

    total_fuel = fuel + reserve_fuel

    print("Fuel required:", round(total_fuel, 2), "litres")

    if total_fuel <= capacity:
        cost = total_fuel * price

        print("Status: Feasible")
        print("Journey cost: Rs.", round(cost, 2))

        if cost < best_cost:
            best_cost = cost
            best_vehicle = name

    else:
        print("Status: Not Feasible")
        print("Required fuel exceeds tank capacity")

print("\n----- FINAL RESULT -----")

if best_vehicle != "":
    print("Lowest cost vehicle:", best_vehicle)
    print("Minimum journey cost: Rs.", round(best_cost, 2))
else:
    print("No feasible vehicle available")

print("Program Completed")

