

n = int(input("Enter number of subjects: "))

max_marks = int(input("Enter maximum marks per subject: "))
pass_marks = int(input("Enter minimum pass marks: "))
grace_limit = int(input("Enter maximum grace marks allowed: "))

marks = []
final_marks = []

for i in range(n):
    m = int(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(m)

print("\n----- EXAMINATION RESULT -----")

for i in range(n):
    m = marks[i]

    if m >= pass_marks:
        final = m
        print("Subject", i + 1, ": PASS")

    elif m + grace_limit >= pass_marks:
        grace = pass_marks - m
        final = min(m + grace, max_marks)
        print("Subject", i + 1, ": PASS with", grace, "grace marks")

    else:
        final = m
        print("Subject", i + 1, ": FAIL")

    final_marks.append(final)

    print("Original Marks:", m)
    print("Final Marks:", final)

total = sum(final_marks)
percentage = (total / (n * max_marks)) * 100

print("\nTotal Marks:", total)
print("Percentage:", round(percentage, 2), "%")

if all(m >= pass_marks for m in final_marks):
    print("Final Result: PASS")

    if percentage >= 75:
        print("Classification: Distinction")
    elif percentage >= 60:
        print("Classification: First Class")
    elif percentage >= 50:
        print("Classification: Second Class")
    else:
        print("Classification: Pass Class")
else:
    print("Final Result: FAIL")
    print("Classification: Not Classified")

