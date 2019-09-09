import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    i = j = 0
    ans = 0

    while i < len(str2):
        if str1[j] != str2[i]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == len(str1):
            ans = 1
            break

    print("#%d %d" % (test_case, ans))



