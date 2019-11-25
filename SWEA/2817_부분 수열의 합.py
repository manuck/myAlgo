import sys
sys.stdin = open('2817_input.txt')

import itertools
t = int(input())

for case in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    sol = 0
    for i in range(1, n+1):
        for j in itertools.combinations(a, i):
            if sum(j) == k:
                sol += 1

    print(f'#{case+1} {sol}')