
import csv

students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({
            "name": row["name"],
            "marks": int(row["marks"])
        })

total = 0
topper = students[0]

for student in students:
    total += student["marks"]

    if student["marks"] > topper["marks"]:
        topper = student

average = total / len(students)

print("Total:", total)
print("Average:", average)
print("Topper:", topper["name"])
print("Topper Marks:", topper["marks"])

print("\nStudent Grades:\n")

for student in students:
    marks = student["marks"]

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print(student["name"], "-", marks, "- Grade", grade)
