import sys
sys.stdin = open('2048 Game_input.txt')

t = int(input())

for case in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # print(a)
    a.sort()
    ans = False
    index = 0
    while a:
        if 2048 in a:
            ans = True
            break
        # print(a)
        if len(a) == 1:
            break
        first = a.pop(0)
        if first == 2048:
            ans = True

        second = a.pop(0)

        if first == second:
            index2 = -1
            for i in range(len(a)):
                if first != a[i]:
                    index2 = i
                    break
            if index2 == -1:
                a.append(first+second)
            else:
                a.insert(index2, first+second)

        else:
            a.insert(0, second)


    if ans == True:
        print('YES')
    else:
        print('NO')