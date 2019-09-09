import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    cnt = [0] * 26

    for ch in str2:
        pos = ord(ch) - ord('A')    # ord('A'):문자의 유니코드값 반환
        cnt[pos] += 1

    Max = 0
    for ch in str1:
        pos = ord(ch) - ord('A')
        Max = cnt[pos] if cnt[pos] > Max else Max

    print("#%d %d" % (test_case, Max))


