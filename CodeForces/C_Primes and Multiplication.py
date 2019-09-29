import sys
sys.stdin = open('C_Primes and Multiplication_input.txt')

import math

x, n = map(int, input().split())

num = [x for x in range(1, x+1)]
num.insert(0, 1)
for i in range(2, x+1):
    j = 2
    while x >= i*j:
        num[i*j] = 1
        j += 1
for l in num:
    if l!=1 and 2<=l and l<=x:
        print(l)






# ans = 1
# for i in range(2, x+1):
#     chk = True
#     for j in range(2, i):
#         if i % j == 0:
#             chk = False
#             break
#     if chk:
#         # print(i)
#         cnt = 0
#         sol = 0
#         while True:
#             if i**cnt > n:
#                 break
#             if i**cnt <= n:
#                 if i**cnt % n == 0:
#                     sol = cnt
#             cnt += 1
#         # print(i, sol)
#         # print(i**sol)
#         ans *= (i**sol)
# print(ans)
