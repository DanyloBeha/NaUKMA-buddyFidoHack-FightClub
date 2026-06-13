N, M = map(int, input().split())
for row in [["#" if (i+j) % 2 == 0 else "." for i in range(M)] for j in range(N)]:
    print("".join(row))