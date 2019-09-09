# 반환값을 가지는 DFS() 함수
# visit[][] 사용하지 않고, 길을 벽으로 설정하고 돌아올때 북구하기
import sys
sys.stdin = open("4875.txt", "r")


sx = sy = ex = ey = 0               # 출발, 도착
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def DFS(x, y):

    if maze[x][y] == '3':
        return True

    maze[x][y] = '1'

    for (dx, dy) in diff:
        tx, ty = x + dx, y + dy

        if tx < 0 or tx == N or ty < 0 or ty == N:
            continue
        if maze[tx][ty] == '1':
            continue
        if DFS(tx, ty):
            maze[x][y] = '0'
            return True

    maze[x][y] = '0'
    return False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = []

    for i in range(N):
        maze.append(list(input()))
        for j in range(N):
            if maze[i][j] == '2':
                sx, sy = i, j
            elif maze[i][j] == '3':
                ex, ey = i, j

    print("#%d %d" % (test_case, DFS(sx, sy)))

