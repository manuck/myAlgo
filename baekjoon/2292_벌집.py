import sys
sys.stdin = open('2292_input.txt')

t = int(input())

for case in range(t):
    n = int(input())
    answer = 0
    value = 1
    a = 0
    for i in range(n):
        a += i
        value = (6*a)+1
        answer += 1
        if value >= n:
            break
    print(answer)