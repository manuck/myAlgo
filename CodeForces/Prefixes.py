import sys
sys.stdin = open('Prefixes_input.txt')

n = int(input())
a = list(input())
# print(a)
acnt = 0
bcnt = 0
ans = 0
for i in range(len(a)):
    if acnt != bcnt and a[i] == a[i-1]:
        if acnt > bcnt:
            if a[i] == 'a':
                a[i] = 'b'
                bcnt += 1
                ans += 1
        else:
            if a[i] == 'b':
                a[i] = 'a'
                acnt += 1
                ans += 1

    else:
        if a[i] == 'a':
            acnt+=1
        else:
            bcnt+=1

print(ans)
print(''.join(a))
