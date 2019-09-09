import sys; sys.stdin = open('input.txt', 'r')


def find():
    for idx in range(N):
        for s in range(N - M + 1):
            e = s + M - 1
            for i in range(M//2):
                if arr[idx][s + i] != arr[idx][e - i]:
                    break
            else:
                print(arr[idx][s:s + M])
                return

            for i in range(M // 2):
                if arr[s + i][idx] != arr[e - i][idx]:
                    break
            else:
                for j in range(s, s + M):
                    print(arr[j][idx], end='')
                print()
                return
    return

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    print('#{} '.format(tc), end='')
    find()
