import sys
sys.stdin = open('2105_input.txt')

t = int(input())

for case in range(1):
    n = int(input())
    g = []
    for i in range(n):
        g.append(list(map(int, input().split())))

    print(g)