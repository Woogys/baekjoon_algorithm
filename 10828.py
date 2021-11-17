from sys import stdin   # 여러 줄을 입력받는 경우 input()은 시간초과 발생 가능하므로
                        # sys모듈의 stdin.readline을 써야함!
x = int(stdin.readline())
stack = []

for i in range(x):
    word = stdin.readline().split()    # ex) order2 -> order | 2 로 쪼개져서
    order = word[0]                    # order자리(word의 0번째)에 아래 명령들이 담기게 됨

    if order == 'push':
        value = word[1]
        stack.append(value)

    elif order == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, x):
#         new_head = Node(x)
#         new_head.next = self.head
#         self.head = new_head
#         return
#
#     def pop(self):
#         if self.empty():
#             return -1
#         delete_head = self.head
#         self.head = self.head.next
#         return delete_head
#
#     def size(self):
#         return len(self)
#
#     def empty(self):
#         if not self:
#             print(1)
#         else:
#             print(0)
#
#     def top(self):
#         if not self:
#             print(-1)
#         else:
#             print(self[-1])
