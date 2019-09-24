import sys
sys.stdin = open('B_Ania and Minimizing_input.txt')

n, k = map(int, input().split())
a = list(input())

if len(a) == 1 and k > 0:
    a[0] = 0
    k = 0
for i in range(len(a)):
    if k == 0:
        break
    if i == 0 and a[i] != '1':
        a[i] = 1
        k -= 1
    elif i == 0 and a[i] == '1':
        continue
    else:
        if a[i] != '0':
            a[i] = 0
            k -= 1

for i in range(len(a)):
    print(a[i],end="")