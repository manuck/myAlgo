import sys
sys.stdin = open('주식가격_input.txt')


prices = list(map(int, input().split()))
answer = []
print(prices)
for i in range(len(prices)):
    state = False
    for j in range(i+1, len(prices)):
        if prices[i] > prices[j]:
            answer.append(j-i)
            state = True
            break
    if state == False:
        answer.append(len(prices)-i-1)
print(answer)








# for i in range(len(prices)-1):
#     fin = False
#     for j in range(i+1, len(prices)):
#         if prices[i] > prices[j]:
#             answer.append(j-i)
#             fin = True
#             break
#     if fin == False:
#         answer.append(len(prices)-i-1)

# answer.append(0)
# print(answer)