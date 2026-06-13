stack = []
input_str = input()
is_correct = True

for char in input_str:
    if char == "(":
        stack.append(char)
    else:
        if not stack:
            is_correct = False
            break
        top = stack.pop()

if is_correct and not stack:
    print("YES")
else:
    print("NO")