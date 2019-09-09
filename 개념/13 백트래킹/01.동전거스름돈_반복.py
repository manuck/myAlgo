coin = [6, 4, 1]

def coinChange(n):
    memo = [0] * (n + 1)

    for money in range(1, n + 1):
        MIN = 0xfffff
        for i in range(len(coin)):
            if coin[i] > money:
                continue
            MIN = min(MIN, memo[money - coin[i]] + 1)

        memo[money] = MIN

    return memo


arr = coinChange(8)
print(arr[1:])
