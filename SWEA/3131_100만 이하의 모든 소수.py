import sys
sys.stdin = open('3131_input.txt')


n = 1000000
a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        # primes.append(i)
        print(i, end=" ")
        for j in range(2*i, n+1, i):
            a[j] = False

