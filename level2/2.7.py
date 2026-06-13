N = int(input())
res = set()

for _ in range(N):
    l = int(input())
    arr = list(map(int, input().split()))
    for n in arr:
        res.add(n)

print(" ".join(list(map(str, sorted(res)))))

# ????????