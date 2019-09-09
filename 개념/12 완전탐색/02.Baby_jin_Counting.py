arr = [0, 5, 4, 0, 6, 0]
#arr = [1, 0, 1, 1, 2, 3]


cnt = [0] * 10

for val in arr:
    cnt[val] += 1


run = triplet = 0
num = 0
while num < 10:
    if cnt[num] >= 3:
        triplet += 1
        cnt[num] -= 3
        continue

    if num <= 7 and cnt[num] and cnt[num + 1] and cnt[num + 2]:
        run += 1
        cnt[num] -= 1
        cnt[num + 1] -= 1
        cnt[num + 2] -= 1
        continue

    num += 1


if run + triplet == 2:
    print("Baby_Jin!!!!")
else:
    print("Fail!!!!")

