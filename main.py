
students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Aman", "marks": 92},
    {"name": "Priya", "marks": 78},
    {"name": "Rohit", "marks": 95},
    {"name": "Neha", "marks": 88}
]

for student in students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("----------------")


total = 0
topper = students[0]

for student in students:
    total += student["marks"]

    if student["marks"] > topper["marks"]:
        topper = student

average = total / len(students)

print("\n========== RESULT ==========")
print("Total Marks:", total)
print("Average Marks:", average)
print("Topper:", topper["name"])
print("Topper Marks:", topper["marks"])
