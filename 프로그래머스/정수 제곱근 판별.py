import sys
sys.stdin = open('정수 제곱근 판별_input.txt')


t = int(input())

for case in range(t):
    n = int(input())
    answer = 0
    if int(n**(1/2)) == (n**(1/2)):
        answer = int((n**(1/2)+1)**2)
    else:
        answer = -1

    print(answer)