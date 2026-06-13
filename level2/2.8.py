first = input()
second = input()

LCS_max_len = -1
LCS_max_str = ""

LCS_len = 0
LCS_str = ""
i = 0
j = 0
while i < len(first):
    if first[i] == second[j]:
        if j == 0:
            LCS_len = 1
            LCS_str = first[i]
        else:
            LCS_len += 1
            LCS_str += first[i]
        j += 1
        
    else:
        j = 0

    if LCS_len > LCS_max_len:
        LCS_max_len = LCS_len
        LCS_max_str = LCS_str
    i += 1

print(LCS_max_len)
print(LCS_max_str)