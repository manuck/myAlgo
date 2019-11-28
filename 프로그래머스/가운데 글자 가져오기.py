import sys
sys.stdin = open('가운데 글자 가져오기_input.txt')


s = list(input())
answer = ''
# print(s[len(s)//2])
if len(s) % 2 == 1:
    answer = s[(len(s)//2)]
else:
    answer += s[len(s)//2-1]
    answer += s[len(s)//2]

print(answer)
