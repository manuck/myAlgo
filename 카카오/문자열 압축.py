import sys
sys.stdin = open('문자열 압축_input.txt')




s = list(input())
print(s)
print(len(s))
ans = 99999999999
for i in range(1, len(s)//2+1):
    ret = 0
    before, cnt = s[:i], 1
    for j in range(i, len(s), i):
        word = s[j:j+i]
        if word == before:
            cnt += 1
        else:
            if cnt > 1:
                ret += len(str(cnt))
            ret += i
            before, cnt = word, 1
    if cnt > 1:
        ret += len(str(cnt))
    ret += len(before)
    ans = min(ans, ret)

if ans == 99999999999:
        ans = 1
print(ans)
