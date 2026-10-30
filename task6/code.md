

## 1. Problem Statement

Develop a Python program to simulate water tank levels over multiple days. The program should process changing water inflow and outflow quantities, update water levels, detect overflow and water shortages, and determine the first day on which the tank reaches a specified threshold.

## 2. Algorithm

1. Start.
2. Enter the tank capacity.
3. Enter the initial water level.
4. Enter the required threshold level.
5. Enter the number of days.
6. For each day:
   - Enter water inflow.
   - Enter water outflow.
   - Calculate the new water level.
   - If the water level exceeds tank capacity, detect overflow.
   - If the water level becomes negative, detect shortage.
   - Update the water level within valid limits.
   - Check whether the threshold is reached for the first time.
7. Display daily water levels.
8. Display overflow and shortage information.
9. Display the first day the threshold is reached.
10. Stop.

## 3. Flowchart – Mermaid Code

Copy this Mermaid code into [Mermaid Live Editor](https://mermaid.live/?utm_source=chatgpt.com) to generate your flowchart.

```

flowchart TD
    A([START]) --> B[/Enter Tank Capacity/]
    B --> C[/Enter Initial Water Level/]
    C --> D[/Enter Threshold Level/]
    D --> E[/Enter Number of Days/]
    E --> F[Set Day = 1]
    F --> G{Day <= Number of Days?}

    G -- No --> P[/Display Final Summary/]
    P --> Q([STOP])

    G -- Yes --> H[/Enter Inflow and Outflow/]
    H --> I[Calculate New Level]
    I --> J[Water Level + Inflow - Outflow]

    J --> K{New Level > Capacity?}
    K -- Yes --> L[Record Overflow]
    K -- No --> M{New Level < 0?}

    L --> N[Set Level = Capacity]
    M -- Yes --> O[Record Shortage]
    M -- No --> R[Update Water Level]
    O --> S[Set Level = 0]

    N --> T{Threshold Reached First Time?}
    R --> T
    S --> T

    T -- Yes --> U[Record First Day]
    T -- No --> V[Continue]
    U --> V
    V --> W[Display Daily Water Level]
    W --> X[Increment Day]
    X --> G

```

## 4. Python Source Code

```
# Experiment 16: Multi-Day Water Tank Simulationcapacity = float(input("Enter tank capacity: "))level = float(input("Enter initial water level: "))threshold = float(input("Enter threshold level: "))days = int(input("Enter number of days: "))overflow_count = 0shortage_count = 0first_threshold_day = -1if (capacity <= 0 or level < 0 or level > capacity        or threshold < 0 or threshold > capacity or days <= 0):    print("Invalid tank details")else:    for day in range(1, days + 1):        print("\nDay", day)        inflow = float(input("Enter water inflow: "))        outflow = float(input("Enter water outflow: "))        if inflow < 0 or outflow < 0:            print("Invalid inflow or outflow")            continue        new_level = level + inflow - outflow        if new_level > capacity:            overflow = new_level - capacity            print("Overflow:", overflow)            overflow_count += 1            level = capacity
```

## 5. Sample Input

```
Enter tank capacity: 1000
Enter initial water level: 500
Enter threshold level: 800
Enter number of days: 4

Day 1
Enter water inflow: 200
Enter water outflow: 100

Day 2
Enter water inflow: 300
Enter water outflow: 50

Day 3
Enter water inflow: 400
Enter water outflow: 100

Day 4
Enter water inflow: 100
Enter water outflow: 200
```

## 6. Sample Output

```
Day 1
Current Water Level: 600.0

Day 2
Current Water Level: 850.0
Threshold Reached on Day: 2

Day 3
Overflow: 150.0
Current Water Level: 1000.0

Day 4
Current Water Level: 900.0

----- WATER TANK SUMMARY -----
Final Water Level: 900.0
Overflow Days: 1
Shortage Days: 0
First Threshold Day: 2
Simulation Completed
```

## 7. Important Formulas

- New water level = Previous water level + Inflow − Outflow
- Overflow = New water level − Tank capacity
- Shortage = Absolute value of negative water level
- If water exceeds capacity, the tank level is limited to its capacity.
- If water becomes negative, the tank level is set to zero.

Flowchart copying: Click inside the Mermaid code box, select all with `Ctrl + A`, and copy using `Ctrl + C`. Paste it into Mermaid Live Editor to view the diagram.
