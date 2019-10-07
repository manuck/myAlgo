import sys
sys.stdin = open('A_CME_input.txt')

t = int(input())

for case in range(t):
    n = int(input())
    ans = 0
    if n < 4:
        ans = 4 - n
    else:
        if n % 2 == 0:
            ans = 0
        else:
            ans = 1

    print(ans)