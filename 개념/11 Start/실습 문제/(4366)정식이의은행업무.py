bin = [0 for _ in range(41)]
tri = [0 for _ in range(41)]
bin[0] = tri[0] = 1
for i in range(1, 40):
    bin[i] = bin[i - 1] << 1
    tri[i] = tri[i - 1] * 3

N = M = 0


def findVal(aval, bval):
    global N, M
    for i in range(N):
        atmp = btmp = 0
        if A[i] == 1:
            atmp = aval - bin[N - 1 - i]
        else:
            atmp = aval + bin[N - 1 - i]

        for j in range(M):
            for k in range(3):
                if k == B[j]:
                    continue

                btmp = bval + (k - B[j]) * tri[M - 1 - j]

                if atmp == btmp:
                    return atmp
    return -1


T = int(input())
for test_case in range(1, T + 1):

    A = []
    B = []

    tmp = input()
    for val in tmp:
        A.append(int(val))

    tmp = input()
    for val in tmp:
        B.append(int(val))

    N, M = len(A), len(B)

    aval = bval = 0
    for i in range(len(A)):
        aval += bin[N - 1 - i] * A[i]
    for i in range(len(B)):
        bval += tri[M - 1 - i] * B[i]

    print('#%d %d' % (test_case, findVal(aval, bval)))