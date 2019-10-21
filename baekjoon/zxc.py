import sys
sys.stdin = open('zxc_input.txt')

a = list(input())
# print(a)
b = set(a)
print(len(b))
# sol = []
# for i in range(len(a)):
#     if not a[i] in sol:
#         sol.append(a[i])
#     if len(sol) >= 20:
#         break
# print(len(sol))