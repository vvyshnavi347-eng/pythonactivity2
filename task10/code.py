

n = int(input("Enter number of applicants: "))

course = input("Enter course name: ")
pass_marks = int(input("Enter minimum subject pass marks: "))
threshold = float(input("Enter minimum aggregate percentage: "))

eligible = []

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter applicant name: ")

    maths = int(input("Enter Mathematics marks: "))
    physics = int(input("Enter Physics marks: "))
    chemistry = int(input("Enter Chemistry marks: "))

    total = maths + physics + chemistry
    aggregate = (total / 300) * 100

    print("Total Marks:", total)
    print("Aggregate:", round(aggregate, 2), "%")

    if (maths >= pass_marks and
        physics >= pass_marks and
        chemistry >= pass_marks and
        aggregate >= threshold):

        eligible.append((name, maths, aggregate))
        print("Admission Status: Eligible")

    else:
        print("Admission Status: Not Eligible")

# Sort by aggregate and Mathematics marks
eligible.sort(key=lambda x: (x[2], x[1]), reverse=True)

print("\n----- UNIVERSITY ADMISSION RANKING -----")
print("Course:", course)

if len(eligible) > 0:
    for i in range(len(eligible)):
        print("\nRank:", i + 1)
        print("Name:", eligible[i][0])
        print("Mathematics Marks:", eligible[i][1])
        print("Aggregate:", round(eligible[i][2], 2), "%")
else:
    print("No eligible applicants found")

print("\nProgram Completed")

