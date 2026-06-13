N = int(input())
arr = list(map(int, input().split()))
N2 = int(input())


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    res = None

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            res = mid
            high = mid - 1
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return res

for _ in range(N2):
    num = int(input())
    res = binary_search(arr, num)
    if res is not None:
        print(res)
    else:
        print(-1)
    
