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
