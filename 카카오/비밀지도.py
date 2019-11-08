import sys
sys.stdin = open("비밀지도_input.txt")

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print(n)
print(arr1)
print(arr2)
answer = []
map1 = [[0 for _ in range(n)]for _ in range(n)]
map2 = [[0 for _ in range(n)]for _ in range(n)]
map3 = [[0 for _ in range(n)]for _ in range(n)]
for i in range(n):
    map1_Num = arr1[i]
    map2_Num = arr2[i]
    for j in range(n):
        if map1_Num >= (2**(n-1-j)):
            map1[i][j] = 1
            map1_Num = map1_Num % (2**(n-1-j))

        if map2_Num >= (2 ** (n - 1 - j)):
            map2[i][j] = 1
            map2_Num = map2_Num % (2 ** (n - 1 - j))


for i in range(n):
    for j in range(n):
        if map1[i][j] == 0 and map2[i][j] == 0:
            map3[i][j] = ' '
        else:
            map3[i][j] = '#'

for i in range(n):
    # print(map3[i])
    answer.append(''.join(map3[i]))

print(answer)

