import sys
sys.stdin = open('14501_input.txt')

def go(index, sum):
    # print(index)
    global ans, n
    if index == n:
        if sum > ans:
            ans = sum
        return
    if index > n:
        return
    go(index + a[index][0], sum + a[index][1])
    go(index + 1, sum)



n = int(input())
a = []
ans = 0
for i in range(n):
    a.append(list(map(int,input().split())))

go(0, 0)

print(ans)