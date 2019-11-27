import sys
sys.stdin = open('모의고사_input.txt')

answers = list(map(int, input().split()))
answer = []
a = [1, 2, 3, 4, 5]
b = [2, 1, 2, 3, 2, 4, 2, 5]
c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
a_cnt = 0
b_cnt = 0
c_cnt = 0
for i in range(len(answers)):
    if answers[i] == a[i % len(a)]:
        a_cnt += 1
    if answers[i] == b[i % len(b)]:
        b_cnt += 1
    if answers[i] == c[i % len(c)]:
        c_cnt += 1
sol = [[1, a_cnt], [2, b_cnt], [3, c_cnt]]
sol.sort(key=lambda x: x[1], reverse=True)
answer.append(sol[0][0])
# print(sol)
for i in range(2):
    if sol[i][1] == sol[i+1][1]:
        answer.append(sol[i+1][0])
    else:
        break
print(answer)