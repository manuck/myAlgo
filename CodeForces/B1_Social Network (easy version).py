import sys
sys.stdin = open('B1_Social Network (easy version)_input.txt')

n, k = map(int, input().split())

a = list(map(int, input().split()))

# print(n, k)
# print(a)

sol = []

for i in range(len(a)):
    if not a[i] in sol:
        sol.insert(0, a[i])
    if len(sol) > k:
        sol.pop()
print(len(sol))
for i in range(len(sol)):
    print(sol[i], end=" ")