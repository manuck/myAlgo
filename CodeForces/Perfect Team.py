import sys
sys.stdin = open('Perfect Team_input.txt')

t = int(input())

for case in range(t):
    m, c, x = map(int, input().split())
    all = m + c + x
    maxteam = all//3
    mc = min(m, c)
    print(min(mc, maxteam))