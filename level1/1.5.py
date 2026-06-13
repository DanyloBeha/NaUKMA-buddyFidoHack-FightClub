N = int(input())
errors = {}
for _ in range(N):
    error = input()
    if error not in errors:
        errors[error] = 1
    else:
        errors[error] += 1


res = ""
m = -1
for key in errors.keys():
    if errors[key] > m:
        m = errors[key]
        res = key

print(res)