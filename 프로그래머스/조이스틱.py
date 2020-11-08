import sys
sys.stdin = open('조이스틱_input.txt')

'''
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
'''

def solution(name):
    answer = 0
    # 순방향 인덱스 a, 역방향 인덱스 b
    a = 1
    b = len(name) - 1
    # 0인덱스위치 answer 더하기
    answer += min(ord(name[0])-ord('A'), ord('Z')-ord(name[0])+1)
    # 순방향 합 a_sum, 역방향 합 b_sum
    a_sum = 0
    b_sum = 0
    # 'A' 카운터 cnt
    cnt = 0
    # 마지막 연속된 'A'의 숫자 카운트
    a_cnt = 0
    b_cnt = 0
    # 전부 'A'면 리턴 0
    for i in range(len(name)):
        if name[i] == 'A':
            cnt += 1
        if cnt == len(name):
            return 0
    # name 한자리면 바로 리턴
    if len(name) == 1:
        return answer
    # 순방향, 역방향 각자 더하기
    for i in range(len(name)-1):
        a_sum += min(ord(name[a]) - ord('A'), ord('Z') - ord(name[a]) + 1)
        b_sum += min(ord(name[b]) - ord('A'), ord('Z') - ord(name[b]) + 1)
        # 역방향 연속된 'A' 카운트는 a_cnt로, 순방향은 b_cnt로 반대로 줌
        if name[a] == 'A' and name[a-1] == 'A':
            b_cnt += 1
        if name[b] == 'A' and name[b-1] == 'A':
            a_cnt += 1
        a += 1
        b -= 1
        # 옆으로 이동시 answer + 1
        answer += 1
    a -= 1
    b += 1
    # 합에서 연속된 cnt 빼기
    if name[a] == 'A':
        # a_sum -= 1
        a_cnt += 1
    if name[b] == 'A':
        # b_sum -= 1
        b_cnt += 1
    a_sum -= a_cnt
    b_sum -= b_cnt
    answer += min(a_sum, b_sum)
    return answer


t = int(input())
for case in range(t):
    name = input()
    print(solution(name))