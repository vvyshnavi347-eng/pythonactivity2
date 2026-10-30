

## 1. Problem Statement

Calculate the fuel requirements and journey costs for several vehicles using journey distance, mileage, fuel prices, and reserve fuel requirements. Check whether each vehicle has sufficient fuel capacity and identify the lowest-cost feasible vehicle.

## 2. Algorithm

1. Start.
2. Input the journey distance.
3. Input the required reserve fuel percentage.
4. Input the number of vehicles.
5. For each vehicle:
   - Read vehicle name.
   - Read mileage (km/litre).
   - Read fuel price per litre.
   - Read fuel tank capacity.
6. Calculate fuel required using distance divided by mileage.
7. Add reserve fuel to the calculated fuel requirement.
8. Check whether the required fuel is within tank capacity.
9. If feasible, calculate the journey cost.
10. Compare the costs of all feasible vehicles.
11. Display the lowest-cost feasible vehicle.
12. If no vehicle is feasible, display a suitable message.
13. Stop.

## 3. Flowchart (Copyable)

```

                 START
                   |
                   v
          INPUT JOURNEY DISTANCE
                   |
                   v
          INPUT RESERVE PERCENTAGE
                   |
                   v
           INPUT NUMBER OF VEHICLES
                   |
                   v
             INPUT VEHICLE DETAILS
                   |
                   v
          CALCULATE FUEL REQUIRED
                   |
                   v
             ADD RESERVE FUEL
                   |
                   v
       CHECK FUEL TANK CAPACITY
                   |
                   v
       IS REQUIRED FUEL <= CAPACITY?
              /           \
            YES            NO
             |              |
             v              v
      CALCULATE COST    MARK NOT FEASIBLE
             |              |
             v              |
       COMPARE COSTS         |
             |              |
             +-------+------+
                     |
                     v
             MORE VEHICLES?
               /       \
             YES        NO
              |          |
              v          v
        INPUT NEXT    ANY FEASIBLE
         VEHICLE?      VEHICLE?
                         /    \
                       YES     NO
                        |       |
                        v       v
                  DISPLAY    DISPLAY
                 LOWEST COST NO FEASIBLE
                  VEHICLE     VEHICLE
                        \       /
                         v     v
                           STOP

```

## 4. Python Source Code

```
# Fuel Consumption and Route Comparisondistance = float(input("Enter journey distance (km): "))reserve = float(input("Enter reserve fuel percentage: "))n = int(input("Enter number of vehicles: "))best_cost = float('inf')best_vehicle = ""for i in range(n):    print("\nEnter details of Vehicle", i + 1)    name = input("Enter vehicle name: ")    mileage = float(input("Enter mileage (km/litre): "))    price = float(input("Enter fuel price per litre: "))    capacity = float(input("Enter fuel tank capacity (litres): "))    if mileage <= 0 or price < 0 or capacity < 0:        print("Invalid vehicle details")        continue    fuel = distance / mileage    reserve_fuel = fuel * reserve / 100    total_fuel = fuel + reserve_fuel    print("Fuel required:", round(total_fuel, 2), "litres")    if total_fuel <= capacity:        cost = total_fuel * price        print("Status: Feasible")        print("Journey cost: Rs.", round(cost, 2))
```

## 5. Sample Input

```
Enter journey distance (km): 300
Enter reserve fuel percentage: 10
Enter number of vehicles: 3

Enter details of Vehicle 1
Enter vehicle name: Car
Enter mileage (km/litre): 15
Enter fuel price per litre: 105
Enter fuel tank capacity (litres): 30

Enter details of Vehicle 2
Enter vehicle name: Bike
Enter mileage (km/litre): 40
Enter fuel price per litre: 105
Enter fuel tank capacity (litres): 10

Enter details of Vehicle 3
Enter vehicle name: SUV
Enter mileage (km/litre): 10
Enter fuel price per litre: 105
Enter fuel tank capacity (litres): 25
```

## 6. Sample Output

```
Fuel required: 22.0 litres
Status: Feasible
Journey cost: Rs. 2310.0

Fuel required: 8.25 litres
Status: Feasible
Journey cost: Rs. 866.25

Fuel required: 33.0 litres
Status: Not Feasible
Required fuel exceeds tank capacity

----- FINAL RESULT -----
Lowest cost vehicle: Bike
Minimum journey cost: Rs. 866.25
Program Completed
```

Note: Reserve fuel is calculated as a percentage of the basic fuel requirement. Only vehicles with sufficient tank capacity are considered for the lowest-cost comparison.
