import sys


sys.setrecursionlimit(100000)
def fib(n):
    if n == 0:
        return 0
    n -= 1
    arr = [1, 1]
    for i in range(2, n + 1):
        arr.append((arr[i - 1] + arr[i - 2]) % 1000000007)
    return arr[n]

N = int(input())

for _ in range(N):
    print(fib(int(input())) % 1000000007)
# FAIL