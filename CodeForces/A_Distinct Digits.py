import sys
sys.stdin = open('A_Distinct Digits_input.txt')


a, b = map(int, input().split())

# print(a, b)
sol = True
for i in range(a, b+1):
    sol = True
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    n = ''.join(str(i))
    # print(n)
    for j in range(len(n)):
        cnt[int(n[j])] += 1
    for j in range(10):
        if cnt[j] > 1:
            sol = False
    if sol:
        print(n)
        break

if not sol:
    print(-1)