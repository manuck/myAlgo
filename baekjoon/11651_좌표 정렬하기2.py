import sys
sys.stdin = open('11651_input.txt')

'''
2차원 평면 위의 점 N개가 주어진다. 
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 
다음 출력하는 프로그램을 작성하시오.

첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. 
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
'''

n = int(input())
location = []
for _ in range(n):
    location.append(list(map(int, input().split())))

print(location)
location.sort(key=lambda x: (x[1], x[0]))
print(location)

for i in range(n):
    print(location[i][0], location[i][1])