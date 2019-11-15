import sys
sys.stdin = open('zxc_input.txt')

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# print(A)
# print(B)
A.sort()
B.sort(reverse=True)
sol = 0
for i in range(N):
    sol += A[i]*B[i]
print(sol)