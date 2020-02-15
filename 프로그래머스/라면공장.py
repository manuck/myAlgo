import sys
sys.stdin = open('라면공장_input.txt')

'''
문제 설명
라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다. 
원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고, 
라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
현재 공장에 남아있는 밀가루 수량 stock, 밀가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies), 
원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때, 밀가루가 떨어지지 않고 공장을 운영하기 위해서 
최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 return 하도록 solution 함수를 완성하세요.

dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.

제한사항
stock에 있는 밀가루는 오늘(0일 이후)부터 사용됩니다.
stock과 k는 2 이상 100,000 이하입니다.
dates의 각 원소는 1 이상 k 이하입니다.
supplies의 각 원소는 1 이상 1,000 이하입니다.
dates와 supplies의 길이는 1 이상 20,000 이하입니다.
k일 째에는 밀가루가 충분히 공급되기 때문에 k-1일에 사용할 수량까지만 확보하면 됩니다.
dates에 들어있는 날짜는 오름차순 정렬되어 있습니다.
dates에 들어있는 날짜에 공급되는 밀가루는 작업 시작 전 새벽에 공급되는 것을 기준으로 합니다. 
예를 들어 9일째에 밀가루가 바닥나더라도, 10일째에 공급받으면 10일째에는 공장을 운영할 수 있습니다.
밀가루가 바닥나는 경우는 주어지지 않습니다.
'''
import heapq
stock = int(input())
dates = list(map(int, input().split()))
supplies = list(map(int, input().split()))
k = int(input())

answer = 0
index = 0
h = []
while stock < k:
    for i in range(index, len(dates)):
        print(h)
        if dates[i] <= stock:
            heapq.heappush(h, [-supplies[i], supplies[i]])
            index = i+1
        else:
            break
    stock += heapq.heappop(h)[1]
    answer += 1

print(answer)
'''
stock의 합이 k를 넘어가면 더이상 공급을 받지 않아도 된다. 
그러므로 while의 조건을 stock<k 으로 잡았다. 
기본적으론 남아있는 stock에 따라서 공급을 받을 수 있는 양이 다르게 된다. 
예시에서와 같이 초기 stock이 4이므로 dates의 4일째인 20을 받을 수밖에 없다. 
만약 기간 내에 여러 개의 날에서 공급을 받을 수 있다면 가장 많은 양을 받아오는 것이 적게 공급을 받도록 할 수 있다. 
따라서 이 과정에서 우선순위 큐, 즉 힙을 사용하게 된다. 
stock에 따라서 받을 수 있는 공급들을 리스트에 담고 인덱스를 저장한다. 
그리고 이 리스트 중에서 가장 많은 공급의 양을 빼서 stock에 더한다.
python에서 heapq라는 모듈을 제공해서 힙구조를 만들 수 있도록 한다. 
하지만 이 힙은 최소힙을 제공하므로 힙구조에서 pop을 했을 때 최솟값이 나오게 된다. 
하지만 이 문제에서는 최댓값을 빼야 하므로 최대 힙을 만들도록 한다. 
따라서 힙에 넣을 당시에 heapq.heappush(h,(-supplies[i],supplies[i])) 와 같이 넣어서 
최대힙을 구성하도록 하고 stock+=heapq.heappop(h)[1] 로 값을 빼도록 한다.
'''