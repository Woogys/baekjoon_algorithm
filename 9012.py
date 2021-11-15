t = int(input())

for i in range(t):
    data = input()
    stack = []

    for j in data:
        if j == "(":    # (이면 스택에 push
            stack.append(j)
        elif j == ")":
            if len(stack) != 0 and stack[-1] == "(":  # 스택 길이가 0이 아니고, (로 끝나
                stack.pop()                           # 있으면 (를 pop해서 )랑 짝 맞춤
            else:
                stack.append(")")
                break

    if len(stack) == 0:   # 스택 len이 0이라는 것은 짝이 다 맞아서 스택 리스트에서 pop됐다는 말!
        print("YES")
    else:
        print("NO")