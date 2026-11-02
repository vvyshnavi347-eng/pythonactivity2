

## 1. Problem Statement

Calculate the current attendance percentage of a student and determine the minimum number of consecutive classes the student must attend to reach the required eligibility percentage under different future attendance scenarios.

## 2. Algorithm

1. Start.
2. Read the number of classes attended and total classes conducted.
3. Read the required eligibility percentage.
4. Calculate the current attendance percentage.
5. Display the current attendance percentage.
6. Read the number of future classes the student will attend and miss.
7. Calculate the minimum additional consecutive classes required to reach eligibility.
8. Display the required number of classes for each scenario.
9. Stop.

## 3. Flowchart (Mermaid Code)

              START
                |
                v
     INPUT ATTENDED CLASSES
                |
                v
      INPUT TOTAL CLASSES
                |
                v
    INPUT ELIGIBILITY PERCENTAGE
                |
                v
   CALCULATE CURRENT ATTENDANCE
                |
                v
    DISPLAY ATTENDANCE PERCENTAGE
                |
                v
      INPUT FUTURE SCENARIOS
                |
                v
   INPUT FUTURE ATTENDED CLASSES
                |
                v
     INPUT FUTURE MISSED CLASSES
                |
                v
       CALCULATE NEW ATTENDANCE
                |
                v
     IS ATTENDANCE ELIGIBLE?
           /          \
         YES           NO
          |             |
          v             v
    EXTRA CLASSES    CALCULATE MINIMUM
       = 0           EXTRA CLASSES
          |             |
          |             v
          |       DISPLAY EXTRA CLASSES
          |             |
          +------|------+
                 v
       MORE SCENARIOS AVAILABLE?
             /          \
           YES           NO
            |             |
            v             v
       NEXT SCENARIO     STOP




## 5. Sample Input

```
Enter classes attended: 60
Enter total classes conducted: 100
Enter eligibility percentage: 75
Enter number of future scenarios: 2

Scenario 1
Enter future classes to attend: 10
Enter future classes to miss: 0

Scenario 2
Enter future classes to attend: 5
Enter future classes to miss: 5
```

## 6. Sample Output

```
Current Attendance: 60.0 %

Scenario 1
Attendance after scenario: 63.64 %
Minimum consecutive classes required: 50
Final attendance percentage: 75.0 %

Scenario 2
Attendance after scenario: 59.09 %
Minimum consecutive classes required: 70
Final attendance percentage: 75.0 %

