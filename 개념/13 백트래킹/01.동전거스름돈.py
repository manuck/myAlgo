coin = [6, 4, 1]
sol = []

MIN = 0xfffff
def coinChange(k, n):   # k: 동전수, n: 금액
    global MIN
    if k >= MIN:
        return
    if n == 0:
        if MIN > k:
            MIN = k
            print(sol)
        return

    for i in range(len(coin)):
        if coin[i] > n:
            continue

        sol.append(coin[i])
        coinChange(k + 1, n - coin[i])
        sol.pop()


coinChange(0, 8)
