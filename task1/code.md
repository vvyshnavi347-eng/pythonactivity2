Problem Statement:

Calculate current attendance percentages and determine the minimum consecutive classes required to reach an eligibility threshold.

Algorithm:
1. Start.
2. Read attended classes and total classes.
3. Calculate attendance percentage.
4. Read required attendance percentage.
5. Read future attendance scenarios.
6. Calculate attendance after each scenario.
7. Find additional classes required.
8. Display results.
9. Stop.
Flowchart:
START
  |
  v
INPUT STUDENT MARKS
  |
  v
CALCULATE TOTAL AND AVERAGE
  |
  v
CHECK PASS MARKS
  |
  v
ARE GRACE MARKS REQUIRED?
  |             |
 YES            NO
  |             |
  v             v
APPLY GRACE    KEEP ORIGINAL
MARKS          MARKS
  |             |
  v             |
CHECK RESULT    |
  |             |
  v             v
DISPLAY RESULT
  |
  v
STOP

attended = int(input("Classes attended: "))
held = int(input("Total classes held: "))
target = float(input("Required attendance percentage: "))

if held <= 0 or attended < 0 or attended > held:
    print("Invalid input")
    exit()

if target <= 0 or target > 100:
    print("Invalid target")
    exit()

current = attended / held * 100

print("Current attendance:", round(current, 2), "%")

scenarios = int(input("Number of future scenarios: "))

for i in range(scenarios):

    future_attend = int(input("Future classes attended: "))
    future_miss = int(input("Future classes missed: "))

    a = attended + future_attend
    t = held + future_attend + future_miss

    percentage = a / t * 100

    extra = 0

    while (a + extra) / (t + extra) * 100 < target:
        extra += 1

    print("Scenario", i + 1)
    print("Attendance:", round(percentage, 2), "%")
    print("Additional classes needed:", extra)
    
    sample input
60
100
75
1
10
0

sample output
Current attendance: 60.0 %
Scenario 1
Attendance: 63.64 %
Additional classes needed: 50
