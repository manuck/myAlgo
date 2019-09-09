sel = []
ch = ('a', 'e', 'i', 'o', 'u')
def comb(k, s, mo, ja):
    global L, C
    if k == L:
        if mo > 0 and ja > 1:
            print(''.join(sel))
        return

    for i in range(s, C):
        sel.append(arr[i])
        if arr[i] in ch:
            comb(k + 1, i + 1, mo + 1, ja)
        else:
            comb(k + 1, i + 1, mo, ja + 1)
        sel.pop()

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()

comb(0, 0, 0, 0)

