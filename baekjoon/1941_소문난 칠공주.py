import sys
sys.stdin = open('1941_input.txt')


'''

총 25명의 여학생들로 이루어진 여학생반은 5*5의 정사각형 격자 형태로 자리가 배치되었고, 얼마 지나지 않아 이다솜과 임도연이라는 두 학생이 두각을 나타내며 다른 학생들을 휘어잡기 시작했다. 곧 모든 여학생이 ‘이다솜파’와 ‘임도연파’의 두 파로 갈라지게 되었으며, 얼마 지나지 않아 ‘임도연파’가 세력을 확장시키며 ‘이다솜파’를 위협하기 시작했다.

위기의식을 느낀 ‘이다솜파’의 학생들은 과감히 현재의 체제를 포기하고, ‘소문난 칠공주’를 결성하는 것이 유일한 생존 수단임을 깨달았다. ‘소문난 칠공주’는 다음과 같은 규칙을 만족해야 한다.

    1. 이름이 이름인 만큼, 7명의 여학생들로 구성되어야 한다.
    2. 강한 결속력을 위해, 7명의 자리는 서로 가로나 세로로 반드시 인접해 있어야 한다.
    3. 화합과 번영을 위해, 반드시 ‘이다솜파’의 학생들로만 구성될 필요는 없다.
    4. 그러나 생존을 위해, ‘이다솜파’가 반드시 우위를 점해야 한다. 따라서 7명의 학생 중 ‘이다솜파’의 학생이 적어도 4명 이상은 반드시 포함되어 있어야 한다.

여학생반의 자리 배치도가 주어졌을 때, ‘소문난 칠공주’를 결성할 수 있는 모든 경우의 수를 구하는 프로그램을 작성하시오.
'''

def dfs(x, y, cnt, scnt):
    global ans
    if cnt == 7 and scnt >= 4:
        for i in range(5):
            print(visited[i])
        print()
        ans += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5: continue
            if ny < 0 or ny >= 5: continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if g[nx][ny] == 'S':
                    dfs(nx, ny, cnt+1, scnt+1)
                else:
                    dfs(nx, ny, cnt+1, scnt)
                visited[nx][ny] = 0



g = [list(input()) for _ in range(5)]
# print(g)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0
for i in range(5):
    for j in range(5):
        if g[i][j] == 'S':
            visited = [[0 for _ in range(5)]for _ in range(5)]
            visited[i][j] = 1
            dfs(i, j, 1, 1)

print(ans)