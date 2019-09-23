import sys
sys.stdin = open('3980_input.txt')

'''
챔피언스 리그 결승전을 앞두고 있는 맨체스터 유나이티드의 명장 퍼거슨 감독은 이번 경기에 4-4-2 다이아몬드 전술을 사용하려고 한다.

오늘 결승전에 뛸 선발 선수 11명은 미리 골라두었지만, 어떤 선수를 어느 포지션에 배치해야 할지 아직 결정하지 못했다.

수석코치 마이크 펠란은 11명의 선수가 각각의 포지션에서의 능력을 0부터 100가지의 정수로 수치화 했다. 0은 그 선수가 그 포지션에 적합하지 않다는 뜻이다.

이때, 모든 선수의 포지션을 정하는 프로그램을 작성하시오. 모든 포지션에 선수를 배치해야 하고, 각 선수는 능력치가 0인 포지션에 배치될 수 없다.
'''

def dfs(x):
    global ans, mysum
    if x == 11:
        ans = max(ans, mysum)
        return
    for i in range(11):
        if player[x][i] != 0 and visited[i] == 0:
            visited[i] = 1
            mysum += player[x][i]
            dfs(x + 1)
            visited[i] = 0
            mysum -= player[x][i]

t = int(input())

for case in range(t):
    player = [list(map(int, input().split())) for _ in range(11)]
    visited = [0] * 11
    mysum = 0
    ans = 0
    dfs(0)
    print(ans)
