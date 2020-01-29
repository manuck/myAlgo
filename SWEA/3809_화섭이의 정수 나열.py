import sys
sys.stdin = open('3809_input.txt')

t = int(input())

for case in range(t):
    s = ''
    n = int(input())
    while len(s) != n:
        s += ''.join(input().split())

    c = -1
    while True:
        c += 1
        if str(c) not in s:
            break
    print(f'#{case+1} {c}')