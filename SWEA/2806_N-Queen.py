import sys
sys.stdin = open('2806_input.txt')

def dfs(no):    # 현재행(no)에서 모든 열에 퀸을 놓아보는 경우의 수
    global sol
    if no >= n:
        sol += 1
        return
    for i in range(n):  # 열
        if chk1[i]:continue # 세로방향체크
        if chk2[no+i]:continue  # 우방향 대각선 체크
        if chk3[(n-1)-(no-i)]:continue  # 좌방향 대각선 체크
        chk1[i] = chk2[no + i] = chk3[(n - 1) - (no - i)] = 1   # 퀸 놓기
        dfs(no+1)
        chk1[i] = chk2[no + i] = chk3[(n - 1) - (no - i)] = 0   # 퀸 빼기


t = int(input())

for case in range(t):
    n = int(input())

    arr = [[0 for _ in range(n)] for _ in range(n)]
    chk1 = [0] * n  # 세로열
    chk2 = [0] * n * 2  # 우대각
    chk3 = [0] * n * 2  # 좌대각
    sol = 0
    dfs(0)
    print(f'#{case+1}', end=" ")
    print(sol)