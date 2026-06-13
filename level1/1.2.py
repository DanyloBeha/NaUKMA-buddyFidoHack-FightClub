N = int(input())
rooms = list(map(int, input().split()))

def is_correct(rooms):
    if rooms[0] >= rooms[1] or rooms[-1] >= rooms[-2]:
        return False
    for i in range(1, len(rooms) - 1):
        if (i+1) % 2 == 0 and not (rooms[i-1] < rooms[i] > rooms[i + 1]):
            return False
        if (i+1) % 2 == 1 and not (rooms[i-1] > rooms[i] < rooms[i + 1]):
            return False
    return True


print("YES" if is_correct(rooms) else "NO")
# RECHECK