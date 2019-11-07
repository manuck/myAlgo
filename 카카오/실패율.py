import sys
sys.stdin = open("실패율_input.txt")

from collections import Counter

N = int(input())
stages = list(map(int, input().split()))

answer = []
result = []
stageCnt = Counter(stages)
# print(stageCnt)
for stage in range(1, N+1):
    playCnt = 0
    clear = 0
    # print('---------------')
    for key in stageCnt.keys():
        # print(key)
        if key == stage:
            playCnt += stageCnt[key]
        elif key > stage:
            clear += stageCnt[key]
    if (playCnt + clear) != 0:
        result.append([stage, playCnt / (playCnt + clear)])
    else:
        result.append([stage, 0])
# print(result)
result.sort(key=lambda x: x[1], reverse=True)
for i in range(len(result)):
    answer.append(result[i][0])
print(answer)