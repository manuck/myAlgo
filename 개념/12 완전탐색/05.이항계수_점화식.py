
def binomial(n, r):
    if r == 0 or n == r: return 1
    return binomial(n - 1, r - 1) + binomial(n - 1, r)


print(binomial(5, 3))

print(binomial(10, 3))