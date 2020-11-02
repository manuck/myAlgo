import sys
sys.stdin = open('키패드 누르기_input.txt')

'''
스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.
이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 
엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

'''

t = int(input())

for case in range(t):
    numbers = list(map(int, input().split()))
    hand = input()
    answer = ''
    print(numbers)
    print(hand)
    position = [[1, 3], [0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
    left = [0, 3]
    right = [2, 3]
    for i in range(len(numbers)):
        x = position[numbers[i]][0]
        y = position[numbers[i]][1]
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            left = [x, y]
            answer += 'L'
            # print(left, right, position[numbers[i]])
            # print(x, y)
            # print('L')
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            right = [x, y]
            answer += 'R'
            # print(left, right, position[numbers[i]])
            # print(x, y)
            # print('R')
        else:
            distance_l = abs(x-left[0]) + abs(y-left[1])
            distance_r = abs(x-right[0]) + abs(y-right[1])
            # print(left, right, position[numbers[i]])
            # print(x, y)
            if distance_l > distance_r:
                right = [x, y]
                answer += 'R'
                # print('R')
            elif distance_l < distance_r:
                left = [x, y]
                answer += 'L'
                # print('L')
            else:
                if hand == 'left':
                    left = [x, y]
                    answer += 'L'
                    # print('L')
                else:
                    right = [x, y]
                    answer += 'R'
                    # print('R')
    print(answer)

