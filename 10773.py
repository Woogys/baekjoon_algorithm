from sys import stdin

k = int(stdin.readline())
stack = []


for i in range(k):
    number = int(stdin.readline())
    if number != 0:
        stack.append(number)
    else:
        stack.pop()
print(sum(stack))