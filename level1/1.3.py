N = int(input())
visits = []
d = {}

for _ in range(N):
    name, sum = list(input().split())
    sum = int(sum)

    if name not in d:
        d[name + "_visits"] = 1
        d[name] = sum
    else:
        d[name + "_visits"] += 1
        d[name] += sum


for name in d:
    if name.endswith("_visits"):
        continue
    print(f"{name} {d[name + '_visits']} {d[name]}")