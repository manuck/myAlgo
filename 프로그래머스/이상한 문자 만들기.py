import sys
sys.stdin = open('이상한 문자 만들기_input.txt')

s = list(input())
answer = ''
# print(s)
index = 0
for i in range(len(s)):
    if s[i] == ' ':
        index = -1
    if index % 2 == 0:
        s[i] = s[i].upper()
    else:
        s[i] = s[i].lower()
    index += 1
answer = ''.join(s)
print(answer)