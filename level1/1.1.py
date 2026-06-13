N, limit = map(float, input().split())
marks = list(map(float, input().split()))

avrg = int(sum(marks) / len(marks))
print(avrg)
if avrg >= limit:
    print("PASS")
else:
    print("FAIL")
    