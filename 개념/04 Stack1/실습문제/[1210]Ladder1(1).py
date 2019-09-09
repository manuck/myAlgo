import sys
sys.stdin = open('1210.txt')

for test_case in range(1, 11):
    N = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    x = y = 0
    for i in range(100):
        if arr[99][i] == 2:
            x, y = 99, i
            break

    dir = 0         # 0:위, 1:좌, 2:우
    while x != 0:
        if dir != 2 and y - 1 >= 0 and arr[x][y - 1]:
            dir, y = 1, y - 1
        elif dir != 1 and y + 1 < 100 and arr[x][y + 1]:
            dir, y = 2, y + 1
        else:
            dir, x = 0, x - 1

    print("#%d %d" % (test_case, y))