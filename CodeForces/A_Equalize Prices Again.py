import sys
sys.stdin = open('A_Equalize Prices Again_input.txt')

import math
t = int(input())

for case in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sol = sum(a)/n
    print(math.ceil(sol))