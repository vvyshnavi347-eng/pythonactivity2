

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


  ##FLOWCHART
                START
                |
                v
       Enter Tank Capacity
       and Initial Water Level
                |
                v
        Enter Number of Days
                |
                v
       Enter Inflow and Outflow
                |
                v
       Calculate New Water Level
                |
                v
       Is Level > Tank Capacity?
             /       \
           YES        NO
            |          |
            v          |
       Detect Overflow |
            |          |
            +----+-----+
                 |
                 v
          Is Level < 0?
             /       \
           YES        NO
            |          |
            v          |
       Detect Shortage |
            |          |
            +----+-----+
                 |
                 v
       Check Threshold Level
                 |
                 v
       Record First Threshold
          Reached Interval
                 |
                 v
          Are More Days?
             /       \
           YES        NO
            |          |
            v          v
       Enter Next    Display Final
          Day        Water Report
            |          |
            |          v
            |         STOP
            |
            +----> Calculate
                   New Water Level

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

