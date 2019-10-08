import sys
sys.stdin = open('B_Strings Equalization_input.txt')


t = int(input())

for case in range(t):
    s = list(input())
    t = list(input())
    ans = 'NO'
    for i in range(len(t)):
        if t[i] in s:
            ans = 'YES'
            break
    print(ans)