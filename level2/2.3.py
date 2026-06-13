N = int(input())

students = []
for _ in range(N):
    name, mark, labs = input().split()
    mark, labs = float(mark), int(labs)
    students.append((name, mark, labs))

res = sorted(students, key=lambda x: (-x[1], -x[2], x[0]))
for student in res:
    print(student[0])

# RECHECK IDK HOW ALPHABETICAL SORTING WORKS IN PYTHON