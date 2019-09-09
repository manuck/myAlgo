import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    ans = 0

    for i in range(len(str2) - len(str1) + 1):
        j = 0
        while j < len(str1):
            if str2[i + j] != str1[j]:
                break
            j += 1

        if j == len(str1):
            ans = 1
            break

    print('#%d %d' % (test_case, ans))
