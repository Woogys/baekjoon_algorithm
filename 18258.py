from sys import stdin
from collections import deque

x = int(stdin.readline())
stack = deque([])

for i in range(x):
    word = stdin.readline().split()
    order = word[0]

    if order == 'push':
        stack.append(word[1])

    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.popleft())

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if not stack:
            print(-1)
        else:
            print(stack[0])

    elif order == 'back':
        if not stack:
            print(-1)
        else:
            print(stack[-1])