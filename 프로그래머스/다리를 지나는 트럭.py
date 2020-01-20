import sys
sys.stdin = open('다리를 지나는 트럭_input.txt')


t = int(input())

for case in range(t):
    bridge_length = int(input())
    weight = int(input())
    truck_weights = list(map(int, input().split()))
    answer = 1

    going = []
    total = []
    while True:
        if truck_weights:
            if sum(total) + truck_weights[0] <= weight:
                going.append(bridge_length)
                total.append(truck_weights[0])
                truck_weights.pop(0)
        answer += 1
        for i in range(len(going)):
            going[i] -= 1
        if going[0] == 0:
            going.pop(0)
            total.pop(0)

        # print(answer, end=" ")
        # print(total, end=" ")
        # print(truck_weights)
        if not truck_weights and not going:
            break

    print(answer)