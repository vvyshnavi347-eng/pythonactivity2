

### 1. Problem Statement

To develop a Python program that processes marks obtained by a student in multiple subjects, checks subject-wise pass criteria, applies the specified grace-mark policy, and generates the final result and classification without exceeding the maximum marks.

### 2. Algorithm

1. Start the program.
2. Read the number of subjects.
3. Enter the maximum marks and passing marks for each subject.
4. Enter the student's marks in each subject.
5. Calculate the grace marks required for subjects in which the student has failed.
6. Check whether the grace marks are within the permitted limit.
7. Add grace marks to eligible subjects.
8. Ensure that the final marks do not exceed the maximum marks.
9. Check the pass or fail status of each subject.
10. Calculate the total marks and percentage.
11. Display the final result.
12. Assign the classification based on the percentage:
    - 75% and above – Distinction
    - 60% to 74% – First Class
    - 50% to 59% – Second Class
    - Below 50% – Third Class
13. Stop the program.

flowchart TD
    A([Start]) --> B[/Enter number of subjects/]
    B --> C[/Enter maximum marks, passing marks and grace limit/]
    C --> D[/Enter marks for each subject/]
    D --> E[Calculate marks required to pass]
    E --> F{Is student failed in subject?}
    F -- No --> G[Keep original marks]
    F -- Yes --> H{Required grace marks within limit?}
    H -- Yes --> I[Add grace marks]
    H -- No --> J[Keep original marks]
    I --> K[Check maximum marks limit]
    G --> L[Calculate total and percentage]
    J --> L
    K --> L
    L --> M{All subjects passed?}
    M -- No --> N[Final Result: FAIL]
    M -- Yes --> O{Percentage >= 75%?}
    O -- Yes --> P[Distinction]
    O -- No --> Q{Percentage >= 60%?}
    Q -- Yes --> R[First Class]
    Q -- No --> S{Percentage >= 50%?}
    S -- Yes --> T[Second Class]
    S -- No --> U[Third Class]
    N --> V[/Display final result/]
    P --> V
    R --> V
    T --> V
    U --> V
    V --> W([Stop])


### 3. Sample Input

```
Enter number of subjects: 5

Enter maximum marks: 100
Enter passing marks: 35
Enter grace mark limit: 5

Enter marks for Subject 1: 85
Enter marks for Subject 2: 72
Enter marks for Subject 3: 32
Enter marks for Subject 4: 90
Enter marks for Subject 5: 68
```

### 4. Sample Output

```

Subject 1: 85
Subject 2: 72
Subject 3: 35 (Grace Marks: 3)
Subject 4: 90
Subject 5: 68

Total Marks: 350 / 500
Percentage: 70%

Subject Status: PASS
Final Result: PASS
Classification: FIRST CLASS
```

