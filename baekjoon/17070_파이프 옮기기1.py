import sys
sys.stdin = open('17070_input.txt')


# def dfs(x, y, z):
#
#
#
# n = int(input())
# g = [list(map(int, input().split()))for _ in range(n)]
# dx = [0, 1, 1]
# dy = [1, 0, 1]
# for i in range(n):
#     print(g[i])


N = int(input())
room = [list(map(int, input().split()))for _ in range(N)]
dp = [[[0]*3 for _ in range(16)] for _ in range(16)]
dp[0][1][0] = 1

for j in range(2, N):
    if not room[0][j]:
        dp[0][j][0] = dp[0][j-1][0]

# for i in range(16):
#     print(dp[i])

for i in range(1, N):
    for j in range(2, N):
        if not room[i][j] and not room[i][j-1] and not room[i-1][j]:
            dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
        if not room[i][j]:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
# print('-------------------------------------------------------------------------')
#
# for i in range(16):
#     print(dp[i])


print(sum(dp[N-1][N-1]))

'''

dx, dy = (0, 1, 1), (1, 0, 1)
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def solve(x, y, z):
    res = 0
    if x == n-1 and y == n-1:
        return 1
    for i in range(3):
        if i+z == 1:
            continue
        nx, ny = x+dx[i], y+dy[i]
        if nx >= n or ny >= n or a[nx][ny]:
            continue
        if i == 2 and (a[x][y+1] or a[x+1][y]):
            continue
        res += solve(nx, ny, i)
    return res

print(solve(0, 1, 0))
'''