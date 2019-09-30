import sys
sys.stdin = open('B_Filling the Grid_input.txt')

h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
g = [[0 for _ in range(w)] for _ in range(h)]
# print(h, w)
# print(r)
# print(c)
for i in range(h):
    if r[i] != 0:

        for j in range(r[i]):
            g[i][j] = 1

# for i in range(h):
#     print(g[i])
# print()

for i in range(w):
    if c[i] != 0:
        # print(r[i])
        for j in range(c[i]):
            g[j][i] = 1
rchange = []
for i in range(h):
    change = 0
    for j in range(w):
        if g[i][j] == 1:
            change += 1
        else:
            rchange.append(change)
            break
        if j == w-1:
            rchange.append(change)

cchange = []
for i in range(w):
    change = 0
    for j in range(h):
        if g[j][i] == 1:
            change += 1
        else:
            cchange.append(change)
            break
        if j == h-1:
            cchange.append(change)


ignore = 0
if r == rchange and c == cchange:
    ignore = 1
# for i in range(h):
#     print(g[i])
# print()
# print(rchange)
# print(cchange)
# print(ignore)
ans = 0
for i in range(h):
    for j in range(w):
        if g[i][j] == 0:
            ycnt = 1
            xcnt = 1
            ystate = 0
            xstate = 0
            while True:
                if j-xcnt < 0: break
                if g[i][j-xcnt] == 0:
                    xstate = 1
                    break
                xcnt += 1

            while True:
                if i-ycnt < 0: break
                if g[i-ycnt][j] == 0:
                    ystate = 1
                    break
                ycnt += 1

            if xstate == 1 and ystate == 1:
                # g[i][j] = 3
                ans += 1
# for i in range(h):
#     print(g[i])
# print(ans)
if ignore == 0:
    print(0)
else:
    print((2**ans)%1000000007)