import sys
sys.stdin = open('1697_input.txt')


def bfs(v):
    global k
    visited = [0] * 100001
    q = [v]
    state = False
    cnt = 0
    while q:
        for i in range(len(q)):
            v = q.pop(0)
            if visited[v] != 1:
                visited[v] = 1
                if v == k:
                    state = True
                    break
                if v - 1 >= 0:
                    q.append(v-1)
                if v + 1 <= 100000:
                    q.append(v+1)
                if v * 2 <= 100000:
                    q.append(v*2)
        if state == True:
            break
        cnt += 1
    return cnt

n, k = map(int, input().split())

print(bfs(n))
