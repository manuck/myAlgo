import sys
sys.stdin = open('1405_input.txt')

'''
통제 할 수 없는 미친 로봇이 평면위에 있다. 그리고 이 로봇은 N번의 행동을 취할 것이다.

각 행동에서 로봇은 4개의 방향 중에 하나를 임의로 선택한다. 그리고 그 방향으로 한 칸 이동한다.

로봇이 같은 곳을 한 번보다 많이 이동하지 않을 때, 로봇의 이동 경로가 단순하다고 한다. (로봇이 시작하는 위치가 처음 방문한 곳이다.) 

로봇의 이동 경로가 단순할 확률을 구하는 프로그램을 작성하시오.

예를 들어, EENE와 ENW는 단순하지만, ENWS와 WWWWSNE는 단순하지 않다. (E는 동, W는 서, N은 북, S는 남)
'''

def robot(step, y, x):
    global n
    if visited[y][x] == 1:
        return 0
    if step >= n:
        return 1

    ans = 0
    visited[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        ans += (a[i] / 100) * robot(step+1, ny, nx)

    visited[y][x] = 0
    return ans


a = list(map(int, input().split()))
n = a.pop(0)
visited = [[0 for _ in range(30)] for _ in range(30)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
sol = robot(0, 15, 15)
print(sol)