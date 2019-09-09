arr = "ABCDE"
pick = [" "] * len(arr)


def comb(n, r):
    if n < r:
        return
    if r == 0:
        print(pick)
        return

    pick[r - 1] = arr[n - 1]
    comb(n - 1, r - 1)
    comb(n - 1, r)


comb(5, 3)
