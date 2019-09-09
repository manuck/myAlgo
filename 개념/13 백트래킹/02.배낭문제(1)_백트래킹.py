
w = [5, 4, 6, 3]
v = [10, 40, 30, 50]

N = len(v)
maxW = 10
maxV = 0

def knapsack(k, W, curV):
    global maxV
    if W < 0: return
    if k == N:
        if maxV < curV:
            maxV = curV
            print('최대가치 = %d' % maxV)
    else:

        knapsack(k + 1, W - w[k], curV + v[k])      # k번째 물건을 담는 경우
        knapsack(k + 1, W, curV)                    # k번째 물건을 담지 않는 경우

knapsack(0, maxW, 0)
print(maxV)

