import sys
sys.stdin = open('1157_input.txt')

'''
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

t = int(input())
for case in range(1):
    s = input()
    answer = ''
    s = s.lower()
    print(s)
    q = [0]*26
    index = 0
    n = 0
    for i in s:
        q[ord(i)-97] += 1
        if n < q[ord(i)-97]:
            n = q[ord(i)-97]
            index = ord(i)-97
    print(q)
    print(index)
    m = max(q)
    cnt = 0
    for i in range(len(q)):
        if m == q[i]:
            cnt += 1
        if cnt > 1:
            answer = '?'

    if not answer == '?':
        answer = chr(index+97)
        answer = answer.upper()
    print(answer)
    # q.sort()
    # print(q)
    # if


