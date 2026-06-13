N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

arr3 = list(map(str, sorted(arr1+arr2)))
print(" ".join(arr3))