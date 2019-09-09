# n번째 물건 부터 배낭을 담을지 결정한다.
w = [0, 5, 4, 6, 3]
v = [0, 10, 40, 30, 50]

N = 4
maxW = 10


memo = [[-1] * (maxW + 1) for _ in range(N + 1)]

# 기저 사례 초기화
for i in range(N + 1): memo[i][0] = 0
for i in range(maxW + 1): memo[0][i] = 0

for i in range(1, N + 1):
    for j in range(1, maxW + 1):
        case1 = case2 = 0
        if j >= w[i]:                   # k번째 물건을 담는 경우
            case1 = memo[i - 1][j - w[i]] + v[i]

        case2 = memo[i - 1][j]          # k번째 물건을 담지 않는 경우

        memo[i][j] = case1 if case1 > case2 else case2


print('최대가치 = %d' % memo[N][maxW])

print('----------------------------------')
for i in range(1, N + 1):
    for j in range(1, maxW + 1):
        print('%2d' % memo[i][j], end=' ')
    print()

