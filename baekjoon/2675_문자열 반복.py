import sys
sys.stdin = open('2675_input.txt')

t = int(input())
for case in range(t):
    n, s = map(str, input().split())
    n = int(n)
    answer = ''
    for i in s:
        answer += n*i

    print(answer)