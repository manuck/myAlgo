import sys
sys.stdin = open('야바위_input.txt')

'''
동호는 공과 N개의 컵을 가지고 야바위를 하고 있다. 
N개의 컵은 모두 구별이 가능하고, 일렬로 늘어서 있다. 
처음에 왼쪽에서 첫 번째 컵에 공을 넣어놓는다. 
그리고 앞으로 Q번 두 컵의 위치를 바꾸는데, i번째에는 왼쪽에서 Ai번째 컵과 왼쪽에서 Bi번째 컵의 위치를 바꾼다.

동호는 공이 어떤 컵에 있는지 맞출 수 없도록 하기 위해 정확히 한 번 속임수를 쓰려고 한다.
속임수는 현재 공이 들어있는 컵이 왼쪽에서 i번째 컵이라고 할 때, 
왼쪽에서 i-1번째 컵이나 왼쪽에서 i+1번째 컵으로 공을 순간 이동시키는 것이다.
이 속임수는 컵을 섞는 도중이 아니라면, 어떤 시점에도 가능하다.

동호가 속임수를 사용할 수 있는 모든 가능성을 따져서, 
N개의 컵 중에 컵을 다 섞고 난 다음 공이 들어있을 수 있는 컵의 개수를 구하는 프로그램을 작성하라.

'''


t = int(input())

for case in range(1, t+1):
    n, q = map(int, input().split())
    answer = 0
    # print(n, q)
    cup = [0] * n
    cup[0] = 'ball'
    for i in range(q):
        a, b = map(int, input().split())
        # print(a, b)
        a -= 1
        b -= 1
        cup[a], cup[b] = cup[b], cup[a]
        # print('-----------------------------------')
        # print(cup)
        for j in range(n):
            if cup[j] == 'ball':
                # print('찾다', j)
                if j != 0:
                    cup[j-1] = 1
                if j != n-1:
                    cup[j+1] = 1
                break
    #     print(cup)
    #     print('-----------------------------------')
    # print(cup)
    for i in range(n):
        if cup[i] != 0:
            answer += 1

    print(f'#{case} {answer}')