import sys
sys.stdin = open("10804_input.txt")

'''
‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.

예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.
'''

t = int(input())

for case in range(1, t+1):
    s = input()
    a = list(s)
    a.reverse()
    answer = ''
    for i in a:
        if i == 'b':
            answer += 'd'
        elif i == 'd':
            answer += 'b'
        elif i == 'q':
            answer += 'p'
        else:
            answer += 'q'
    print(f'#{case} {answer}')
