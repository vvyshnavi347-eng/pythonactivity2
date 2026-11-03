

## 1. Problem Statement

Compare student assessment scores across multiple examinations. Calculate improvement or decline in each subject, identify consistently weak subjects, and classify the student using the overall average.

## 2. Objectives

- Analyse student scores across multiple examinations.
- Calculate the average score for each subject.
- Identify improvement or decline in each subject.
- Identify consistently weak subjects.
- Classify overall student performance.

## 3. Assumptions

1. All examination scores must be between 0 and 100.
2. A subject is considered weak when its average score is below 40.
3. Performance classification is based on the overall average:
   - 75 and above – EXCELLENT
   - 60 to 74.99 – GOOD
   - 40 to 59.99 – AVERAGE
   - Below 40 – NEEDS IMPROVEMENT

## 4. Algorithm

1. Start the program.
2. Read the number of subjects and examinations.
3. Read each subject name.
4. Read the marks for every examination.
5. Validate that each mark is between 0 and 100.
6. Calculate the average score for each subject.
7. Calculate the score change by subtracting the first examination score from the last examination score.
8. If the subject average is below 40, identify it as consistently weak.
9. Calculate the overall average of all subjects and examinations.
10. Classify the student's performance.
11. Display the complete performance report.
12. Stop the program.

## 5. Flowchart
             START
               |
               v
  INPUT NUMBER OF SUBJECTS
  AND EXAMINATIONS
               |
               v
       INPUT SUBJECT NAMES
        AND EXAM SCORES
               |
               v
       VALIDATE ALL SCORES
               |
               v
       CALCULATE SUBJECT
            AVERAGE
               |
               v
      CALCULATE IMPROVEMENT
        OR DECLINE
               |
               v
      IS AVERAGE BELOW 40?
          /          \
        YES           NO
         |             |
         v             v
   MARK AS WEAK   SATISFACTORY
         |             |
         +------+------+
                |
                v
       CALCULATE OVERALL
            AVERAGE
                |
                v
       CLASSIFY PERFORMANCE
                |
                v
       DISPLAY FINAL REPORT
                |
                v
               STOP




## 7. Sample Input

```
Number of subjects: 2
Number of examinations: 2
Subject name: Python
Score in exam 1: 55
Score in exam 2: 70
Subject name: Mathematics
Score in exam 1: 35
Score in exam 2: 38
```

## 8. Sample Output

```
Subject: Python
Average: 62.5
Change from first to last: 15.0
Trend: IMPROVEMENT
Status: SATISFACTORY

Subject: Mathematics
Average: 36.5
Change from first to last: 3.0
Trend: IMPROVEMENT
Status: CONSISTENTLY WEAK

Overall average: 51.0
Performance: AVERAGE
```

