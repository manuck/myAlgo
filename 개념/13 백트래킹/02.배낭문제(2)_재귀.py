# 0번 물건부터 시작하기
w = [5, 4, 6, 3]
v = [10, 40, 30, 50]

N = len(v)
maxW = 10

def knapsack(k, W):

    if k == N or W == 0:
        return 0
    else:
        case1 = case2 = 0
        if W >= w[k]:               # k번째 물건을 담는 경우
            case1 = knapsack(k + 1, W - w[k]) + v[k]

        case2 = knapsack(k + 1, W)    # k번째 물건을 담지 않는 경우

        return case1 if case1 > case2 else case2

print('최대가치 = %d' % (knapsack(0, maxW)))



