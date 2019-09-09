coin = [6, 4, 1]
memo = [0] * 100

def coinChange(n):
    if n == 0:
        return 0
    if memo[n]:
        return memo[n]

    MIN = 0xfffff
    for i in range(len(coin)):
        if coin[i] > n:
            continue

        ret = coinChange(n - coin[i]) + 1
        MIN = min(MIN, ret)

    memo[n] = MIN
    return memo[n]


print(coinChange(8))
print(memo[1:9])