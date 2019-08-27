import sys
sys.stdin = open('1759_input.txt')



def comb(n, r, q):
    global res
    if r == 0:
        # print(T)
        z = T[:q]
        # print(z)
        moCnt = 0
        for w in z:
            if (q - moCnt) < 2:
                return
            if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
                moCnt += 1
        if moCnt >= 1 and (q - moCnt) >= 2:
            z.sort()
            res.append(z)
    elif n < r:
        return
    else:
        T[r-1] = myStr[n-1]
        comb(n-1, r-1, q)
        comb(n-1, r, q)


l, c = map(int, input().split())

myStr = list(map(str, input().split()))
T = [0] * c
# print(myStr)
res = []
comb(6, 4, 4)

# print(res)
res.sort()
# print(res)
for i in range(len(res)):
    # print(res[i])
    for j in range(l):
        print(res[i][j], end="")
    print()