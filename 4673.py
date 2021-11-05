# 4673 함수 - 셀프 넘버

def self_number(num):
    self_num = num
    while num != 0:
        self_num += num % 10    # 36 + 6' + 3'' | 36 % 10 = 6' | 3'' % 10 = 3
        num //= 10   # 36 // 10 = 3''    3 // 10 = 0
    return self_num


result = []

for i in range(1, 10001):
    result.append(self_number(i))   # ex) 36
    if i not in result:
        print(i)





















# def d(n):       # 문제 제시 함수 d(n) 정의
#     number = int(n)     # n이라는 숫자를 number라는 변수에 담는다. 정수변환
#     for i in str(n):  # 정수 -> 문자열
#         number += int(i)      # n의 각 자릿수를 number에 더해줌
#     return number
#
#
# non_self_numbers = []     # "셀프 넘버가 아닌 숫자(=생성자가 있는 숫자)" 리스트 정의
# for i in range(1, 10001):   # 이 리스트에 1부터 10000까지 d(n)에 넣고 반복
#     num = d(i)
#     non_self_numbers.append(num)
#
# for j in range(1, 10001):   # j가 리스트에 있으면 통과, 없으면(셀프넘버면) 출력
#     if j in non_self_numbers:
#         pass
#     else:
#         print(j)






# num = set(range(1, 10001))        # 시간 84ms
# rmv = set()
# for i in range(1, 10001):
#     for j in str(i):
#         i += int(j)
#     rmv.add(i)
# num = num - rmv
# for k in sorted(num):
#     print(k)
