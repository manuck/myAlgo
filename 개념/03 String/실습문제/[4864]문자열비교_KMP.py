import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    ans = 0
    skip = [0] * (len(str1) + 1)
    skip[0] = -1
    i = 0
    j = -1

    # next[] 테이블 생성
    while i < len(str1):
        while j >= 0 and str1[j] != str1[i]:
            j = skip[j]
        i += 1
        j += 1
        skip[i] = j

    # 매칭
    i = 0
    j = 0
    while i < len(str2):
        while j >= 0 and str1[j] != str2[i]:
            j = skip[j]
        i += 1
        j += 1
        if j == len(str1):
            ans = 1
            break

    print("#%d %d" % (test_case, ans))




