

## 1. Problem Statement

Evaluate candidates for university admission using subject-wise eligibility, aggregate marks, and course-specific eligibility thresholds. Apply tie-breaking criteria based on aggregate marks and Mathematics marks, and generate a ranked list of eligible applicants.

## 2. Algorithm

1. Start.
2. Input the number of applicants.
3. Input the course name.
4. Input the minimum subject pass marks.
5. Input the minimum aggregate percentage required for admission.
6. For each applicant:
   - Read applicant name.
   - Read Mathematics, Physics, and Chemistry marks.
   - Calculate total marks and aggregate percentage.
   - Check whether each subject meets the minimum pass marks.
   - Check whether the aggregate meets the course eligibility threshold.
7. If all conditions are satisfied, add the applicant to the eligible list.
8. Sort eligible applicants by:
   - Aggregate percentage in descending order.
   - Mathematics marks in descending order when aggregate marks are equal.
9. Display the ranked list of eligible applicants.
10. If no applicants are eligible, display a suitable message.
11. Stop.

## 3. Flowchart (Copyable Text)

```

                  START
                    |
                    v
           INPUT NUMBER OF APPLICANTS
                    |
                    v
             INPUT COURSE DETAILS
                    |
                    v
          INPUT SUBJECT PASS MARKS
                    |
                    v
        INPUT AGGREGATE ELIGIBILITY
                    |
                    v
           INPUT APPLICANT DETAILS
                    |
                    v
       INPUT MATHS, PHYSICS, CHEMISTRY
                    |
                    v
          CALCULATE TOTAL AND AVERAGE
                    |
                    v
         CHECK SUBJECT PASS CRITERIA
                    |
                    v
       CHECK AGGREGATE ELIGIBILITY
                    |
                    v
             IS APPLICANT ELIGIBLE?
                /          \
              YES           NO
               |             |
               v             |
        ADD TO ELIGIBLE      |
             LIST            |
               |             |
               +------|------+
                      |
                      v
             MORE APPLICANTS?
                /          \
              YES           NO
               |             |
               v             v
         INPUT NEXT      SORT ELIGIBLE
          APPLICANT      APPLICANTS
                             |
                             v
                     GENERATE RANKING
                             |
                             v
                     DISPLAY RESULTS
                             |
                             v
                            STOP

```

## 4. Python Source Code

```
# University Admission Decision Enginen = int(input("Enter number of applicants: "))course = input("Enter course name: ")pass_marks = int(input("Enter minimum subject pass marks: "))threshold = float(input("Enter minimum aggregate percentage: "))eligible = []for i in range(n):    print("\nApplicant", i + 1)    name = input("Enter applicant name: ")    maths = int(input("Enter Mathematics marks: "))    physics = int(input("Enter Physics marks: "))    chemistry = int(input("Enter Chemistry marks: "))    total = maths + physics + chemistry    aggregate = (total / 300) * 100    print("Total Marks:", total)    print("Aggregate:", round(aggregate, 2), "%")    if (maths >= pass_marks and        physics >= pass_marks and        chemistry >= pass_marks and        aggregate >= threshold):        eligible.append((name, maths, aggregate))        print("Admission Status: Eligible")    else:        print("Admission Status: Not Eligible")# Sort by aggregate and Mathematics markseligible.sort(key=lambda x: (x[2], x[1]), reverse=True)print("\n----- UNIVERSITY ADMISSION RANKING -----")print("Course:", course)if len(eligible) > 0:    for i in range(len(eligible)):        print("\nRank:", i + 1)        print("Name:", eligible[i][0])        print("Mathematics Marks:", eligible[i][1])        print("Aggregate:", round(eligible[i][2], 2), "%")else:    print("No eligible applicants found")print("\nProgram Completed")
```

## 5. Sample Input

```
Enter number of applicants: 4
Enter course name: Computer Science
Enter minimum subject pass marks: 40
Enter minimum aggregate percentage: 60

Applicant 1
Enter applicant name: Ravi
Enter Mathematics marks: 90
Enter Physics marks: 85
Enter Chemistry marks: 80

Applicant 2
Enter applicant name: Priya
Enter Mathematics marks: 95
Enter Physics marks: 90
Enter Chemistry marks: 85

Applicant 3
Enter applicant name: Kumar
Enter Mathematics marks: 70
Enter Physics marks: 65
Enter Chemistry marks: 60

Applicant 4
Enter applicant name: Sita
Enter Mathematics marks: 35
Enter Physics marks: 80
Enter Chemistry marks: 75
```

## 6. Sample Output

```
Applicant 1
Total Marks: 255
Aggregate: 85.0 %
Admission Status: Eligible

Applicant 2
Total Marks: 270
Aggregate: 90.0 %
Admission Status: Eligible

Applicant 3
Total Marks: 195
Aggregate: 65.0 %
Admission Status: Eligible

Applicant 4
Total Marks: 190
Aggregate: 63.33 %
Admission Status: Not Eligible

----- UNIVERSITY ADMISSION RANKING -----

Course: Computer Science

Rank: 1
Name: Priya
Mathematics Marks: 95
Aggregate: 90.0 %

Rank: 2
Name: Ravi
Mathematics Marks: 90
Aggregate: 85.0 %

Rank: 3
Name: Kumar
Mathematics Marks: 70
Aggregate: 65.0 %

Program Completed
```

Note: Each subject has a maximum of 100 marks. The ranking uses aggregate percentage first and Mathematics marks as the tie-breaker when aggregate percentages are equal.
