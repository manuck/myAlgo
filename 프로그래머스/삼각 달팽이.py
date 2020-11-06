import sys
sys.stdin = open('삼각 달팽이_input.txt')

'''
문제 설명
정수 n이 매개변수로 주어집니다.
 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 
 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.
n은 1 이상 1,000 이하입니다.
'''

t = int(input())
for case in range(t):
    n = int(input())
    answer = []
    g = [[0 for _ in range(n)] for _ in range(n)]
    print(n)
    x, y = 0, -1
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            # print(num, y, x)
            g[y][x] = num
            num += 1
            # print(g)
    # for i in range(n):
    #     print(g[i])
    for i in range(n):
        for j in range(n):
            if g[i][j] != 0:
                answer.append(g[i][j])




    print(answer)