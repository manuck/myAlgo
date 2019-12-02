import sys
sys.stdin = open('최대공약수와 최소공배수_input.txt')

t = int(input())

for case in range(t):
    n, m = map(int, input().split())
    a = n
    b = m
    answer = []
    r = 0
    while b != 0:
        r = a % b
        a = b
        b = r

    answer.append(a)
    answer.append(int(n*m/answer[0]))

    print(answer)

