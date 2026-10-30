

n = int(input("Number of subjects: "))
e = int(input("Number of examinations: "))

if n <= 0 or e <= 0:
    print("Invalid number of subjects or examinations")
    exit()

subjects = []
scores = []

for i in range(n):
    name = input("Subject name: ")
    subjects.append(name)

    row = []

    for j in range(e):
        mark = float(input("Score in exam " + str(j + 1) + ": "))

        if mark < 0 or mark > 100:
            print("Invalid score")
            exit()

        row.append(mark)

    scores.append(row)

total = 0

for i in range(n):
    average = sum(scores[i]) / e
    change = scores[i][-1] - scores[i][0]

    total += sum(scores[i])

    print("\nSubject:", subjects[i])
    print("Average:", round(average, 2))
    print("Change from first to last:", round(change, 2))

    if change > 0:
        print("Trend: IMPROVEMENT")
    elif change < 0:
        print("Trend: DECLINE")
    else:
        print("Trend: NO CHANGE")

    if average < 40:
        print("Status: CONSISTENTLY WEAK")
    else:
        print("Status: SATISFACTORY")

overall = total / (n * e)

print("\nOverall average:", round(overall, 2))

if overall >= 75:
    print("Performance: EXCELLENT")
elif overall >= 60:
    print("Performance: GOOD")
elif overall >= 40:
    print("Performance: AVERAGE")
else:
    print("Performance: NEEDS IMPROVEMENT")

