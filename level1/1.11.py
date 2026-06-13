N = int(input())

students = []

for i in range(N):
    name, serie = input().split()
    students.append((name, serie))

students.sort(key=lambda x: x[0])

longest_streak = -1

current_longest_streak = 0
current_streak = 0
student_with_longest_streak = ""
for student in students:
    for char in student[1]:
        if char == "1":
            current_streak += 1
        else:
            if current_streak > current_longest_streak:
                current_longest_streak = current_streak
                student_with_longest_streak = student[0]
            current_streak = 0
    if current_streak > current_longest_streak:
        current_longest_streak = current_streak
        student_with_longest_streak = student[0]
        current_streak = 0

    if current_longest_streak > longest_streak:
        longest_streak = current_longest_streak
        student_with_longest_streak = student[0]

print(student_with_longest_streak, longest_streak)