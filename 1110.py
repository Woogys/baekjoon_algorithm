# 1110 while문 - 더하기 사이클
#
# n = int(input())   # 입력된 값을 int(정수타입)으로 바꿈
# num = n      # 변하는 값
# count = 0   # 사이클
#
# while True:     # 조건이 참이면 계속 반복함!
#     a = num // 10   # 26일 때 2를 a로, 6을 b로 보면 a는 주어진 수를 10으로 나눈 몫
#     b = num % 10    # b는 10으로 나눈 나머지
#     c = (a + b) % 10    # c는 각 자리수를 더한 값을 10으로 나눈 나머지
#     num = (b * 10) + c  # 문제에서 구해야 하는 것은 b를 10의 자리로, c를 1의 자리로 하는 0보다 크고 99보다 작은 정수
#
#     count += 1  # 사이클이 돌 때마다 1씩 높여준다.
#     if num == n:    # 원래 n과 num이 같아지면 종료(break)
#         break
# print(count)

n = int(input())
num = n
count = 0
while True:
    num = ((num % 10) * 10) + ((num // 10) + (num % 10)) % 10
    count += 1

    if num == n:
        break

print(count)