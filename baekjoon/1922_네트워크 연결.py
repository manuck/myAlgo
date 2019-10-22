import sys
sys.stdin = open('1922_input.txt')

<<<<<<< HEAD

=======
>>>>>>> a7c87541b338e06a48eed1f7596c944b92cd96c7
def find(x):
    if x != b[x]:
        b[x] = find(b[x])
    return b[x]

def mst():
    global ans, cnt
    for a1, a2, a3 in a:
        one = find(a1)
        two = find(a2)
        if one != two:
            b[one] = two
            ans += a3
            cnt += 1
        if cnt == n-1:
            break



n = int(input())
m = int(input())

a = []
b = list(range(n+1))
<<<<<<< HEAD
for i in range(m):
    a.append(list(map(int, input().split())))
ans = 0
cnt = 0
# print(a)
a.sort(key=lambda x: x[2])
# print(a)
# print(b)
=======
ans = 0
cnt = 0

for i in range(m):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: x[2])

>>>>>>> a7c87541b338e06a48eed1f7596c944b92cd96c7
mst()
print(ans)