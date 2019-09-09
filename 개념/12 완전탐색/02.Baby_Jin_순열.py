#arr = [0, 5, 4, 0, 6, 0]
arr = [1, 0, 1, 1, 2, 3]


def check(arr):
    cnt = 0
    if arr[0] == arr[1] and arr[1] == arr[2]:
        cnt += 1
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        cnt += 1
    if arr[3] == arr[4] and arr[4] == arr[5]:
        cnt += 1
    if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]:
        cnt += 1
    return cnt == 2

permcnt = 0
def perm(arr, n, k):
    if n == k:
        global permcnt
        permcnt += 1
        if check(arr):
            return True
        else:
            return False

    for i in range(k, n):
        arr[k], arr[i] = arr[i], arr[k]
        if perm(arr, n, k + 1):
            return True
        arr[k], arr[i] = arr[i], arr[k]

    return False


print(perm(arr, len(arr), 0))
print(permcnt)
