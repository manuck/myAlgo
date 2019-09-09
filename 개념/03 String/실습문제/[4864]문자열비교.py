import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    pos = str2.find(str1, 0)
    ans = 1 if pos != -1 else 0

    print("#%d %d" % (test_case, ans))


