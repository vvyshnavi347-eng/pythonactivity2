

## 1. Problem Statement

Develop a Python program to calculate parking charges based on vehicle entry and exit times, vehicle categories, overnight parking, daily limits, and penalty conditions. The program should also validate time inputs and display the total parking fee.

## 2. Algorithm

1. Start.
2. Enter vehicle category.
3. Enter vehicle entry time and exit time in 24-hour format.
4. Validate the time inputs.
5. Calculate total parking duration.
6. If exit time is earlier than entry time, consider overnight parking.
7. Calculate parking charges based on vehicle category.
8. Apply the daily maximum parking limit.
9. Check penalty conditions.
10. Calculate the final parking fee.
11. Display parking duration and total fee.
12. Stop.

Assumed parking rates for this program:

| Vehicle     | Rate per hour |
| ----------- | ------------- |
| Two-wheeler | ₹10           |
| Car         | ₹20           |
| Bus         | ₹40           |

- Maximum daily charge: ₹200.
- Invalid time or vehicle category is rejected.
- Late parking penalty: ₹50 if parking exceeds 24 hours.
- Partial hours are charged as full hours.

## 3. Flowchart – Mermaid Code

Copy the code below into Mermaid Live Editor.

```

flowchart TD
    A([START]) --> B[/Enter Vehicle Category/]
    B --> C[/Enter Entry Time and Exit Time/]
    C --> D{Are Time Inputs Valid?}
    D -- No --> E[Display Invalid Time]
    E --> Z([STOP])

    D -- Yes --> F{Exit Time < Entry Time?}
    F -- Yes --> G[Calculate Overnight Duration]
    F -- No --> H[Calculate Normal Duration]
    G --> I[Calculate Total Hours]
    H --> I

    I --> J{Vehicle Category?}
    J -- Two Wheeler --> K[Rate = 10 per hour]
    J -- Car --> L[Rate = 20 per hour]
    J -- Bus --> M[Rate = 40 per hour]

    K --> N[Calculate Parking Fee]
    L --> N
    M --> N

    N --> O{Fee > Daily Limit?}
    O -- Yes --> P[Apply Daily Maximum Limit]
    O -- No --> Q[Keep Calculated Fee]
    P --> R{Duration > 24 Hours?}
    Q --> R

    R -- Yes --> S[Add Penalty]
    R -- No --> T[No Penalty]
    S --> U[Calculate Final Fee]
    T --> U

    U --> V[/Display Duration and Final Fee/]
    V --> Z

```

## 4. Python Source Code

```
# Experiment 15: Smart Parking Fee Managementprint("SMART PARKING FEE MANAGEMENT")vehicle = input("Enter vehicle category (bike/car/bus): ").lower()entry = input("Enter entry time (HH:MM): ")exit_time = input("Enter exit time (HH:MM): ")try:    eh, em = map(int, entry.split(":"))    xh, xm = map(int, exit_time.split(":"))    if not (0 <= eh <= 23 and 0 <= xh <= 23            and 0 <= em <= 59 and 0 <= xm <= 59):        print("Invalid time input")    elif vehicle not in ["bike", "car", "bus"]:        print("Invalid vehicle category")    else:        entry_minutes = eh * 60 + em        exit_minutes = xh * 60 + xm        if exit_minutes < entry_minutes:            duration = (24 * 60 - entry_minutes) + exit_minutes        else:            duration = exit_minutes - entry_minutes        hours = (duration + 59) // 60        rates = {            "bike": 10,            "car": 20,            "bus": 40
```

## 5. Sample Input

```
SMART PARKING FEE MANAGEMENT
Enter vehicle category (bike/car/bus): car
Enter entry time (HH:MM): 22:00
Enter exit time (HH:MM): 06:00
```

## 6. Sample Output

```
----- PARKING BILL -----
Vehicle Category: car
Parking Duration: 8 hours 0 minutes
Total Charge: Rs. 160
Penalty: Rs. 0
Final Parking Fee: Rs. 160
```



Flowchart copying tip: Click the Mermaid code box and use its copy icon. If it does not work, select the code with your mouse and press `Ctrl + C`.
