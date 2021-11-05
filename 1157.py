# 1157 문자열 - 단어공부

word = input().upper()  # 마지막 반환을 대문자로 해야하니까 처음부터 대문자로 입력
word_list = list(set(word))  # 입력된 문자의 중복값 제거
count_list = []

for i in word_list:
    count = word.count(i)
    count_list.append(count)  # count 숫자를 리스트에 append

if count_list.count(max(count_list)) > 1:  # count중 max 알파벳이 중복 존재시 ?
    print('?')
else:  # 가장 많이 사용된 알파벳 출력
    print(word_list[count_list.index(max(count_list))])
