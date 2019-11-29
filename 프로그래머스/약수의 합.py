import sys
sys.stdin = open('약수의 합_input.txt')

t = int(input())

for case in range(t):
    n = int(input())
    answer = 0
    visit = [1]*(n+1)
    for i in range(1, n+1):
        if visit[i]:
            if n % i == 0:
                visit[n//i] = 0
                visit[i] = 0
                answer += (n//i)
                answer += i

    print(answer)
