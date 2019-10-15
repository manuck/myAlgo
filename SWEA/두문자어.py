import sys
sys.stdin = open('두문자어_input.txt')


t = int(input())

for case in range(1, t+1):
    a = list(input())
    # print(a)
    ans = [a[0].upper()]
    # print(ans)
    for i in range(len(a)):
        if a[i] == ' ':
            ans.append(a[i+1].upper())

    print(f'#{case}', end=" ")
    print(''.join(ans))