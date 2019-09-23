import sys; sys.stdin = open('1240.txt', 'r')

C = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    def find():
        for i in range(N):
            for j in range(M - 1, -1, -1):
                if arr[i][j] == '0': continue
                pwd = []
                for s in range(j - 56 + 1, j, 7):
                    pwd.append(C[arr[i][s: s + 7]])
                a = b = 0
                a = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                b = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                if (a * 3 + b) % 10 == 0:
                    return a + b
                else: return 0
        return 0

    print('#{} {}'.format(tc, find()))