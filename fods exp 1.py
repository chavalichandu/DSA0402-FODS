import numpy as np

marks = np.array([
    [85, 90, 78],
    [70, 88, 92],
    [95, 89, 96],
    [60, 75, 80],
    [88, 91, 84]
])

total_marks = np.sum(marks, axis=1)

average_marks = np.mean(marks, axis=1)

subject_average = np.mean(marks, axis=0)

highest_mark = np.max(marks)
lowest_mark = np.min(marks)

top_student = np.argmax(total_marks) + 1

passed_students = average_marks >= 40

print("Marks:\n", marks)
print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)
print("Subject-wise Average:", subject_average)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Top Student: Student", top_student)
print("Passed Students:", passed_students)
