import sys
sys.stdin = open('1216.txt')

for test_case in range(1, 11):
    N = input()
    arr = []
    for i in range(100):
        arr.append(input())
    ans = 0
    for line in range(100):
        for start in range(100):
            for end in range(99, start, -1):
                L = end - start + 1
                if L <= ans: break
                cnt = L // 2
                i = 0
                while i < cnt:
                    if arr[line][start + i] != arr[line][end - i]: break
                    i += 1
                if i == cnt: ans = L
                i = 0
                while i < cnt:
                    if arr[start + i][line] != arr[end - i][line]: break
                    i += 1
                if i == cnt: ans = L

    print("#%d %s" % (test_case, ans))