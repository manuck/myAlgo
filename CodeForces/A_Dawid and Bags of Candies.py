import sys
sys.stdin = open('A_Dawid and Bags of Candies_input.txt')


import itertools

a = list(map(int, input().split()))
b = list(itertools.combinations(a, 2))
ans = 'NO'
for i in range(len(b)//2):
    if sum(b[i]) == sum(b[~i]):
        ans = 'YES'

if max(a) == sum(a)-max(a):
    ans = 'YES'

print(ans)