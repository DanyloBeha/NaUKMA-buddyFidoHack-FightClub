N = int(input())
arr = list(map(int, input().split()))


print(f"Min: {min(arr)}")
print(f"Max: {max(arr)}")
print(f"Median: {sorted(arr)[len(arr)//2] if len(arr) % 2 == 1 else (sorted(arr)[len(arr)//2][0] + sorted(arr)[len(arr)//2][1]) / 2}")
print(f"Above average: {len([1 for num in arr if num > sum(arr)/len(arr)])}")