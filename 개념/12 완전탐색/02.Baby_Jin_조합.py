def check(arr):
    ret = False
    if arr[0] == arr[1] and arr[1] == arr[2]:
        ret = True
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        ret = True

    return ret

def babyjin():
    A, B = [], []
    visit = [False] * 6

    for i in range(6):
        A.append(arr[i])
        visit[i] = True
        for j in range(i + 1, 6):
            A.append(arr[j])
            visit[j] = True
            for k in range(j + 1, 6):
                A.append(arr[k])
                visit[k] = True
                for x in range(6):
                    if not visit[x]: B.append(arr[x])

                if check(A) and check(B): return True

                B.clear()
                A.pop()
                visit[k] = False
            A.pop()
            visit[j] = False
        A.pop()
        visit[i] = False

    return False

arr = [0, 5, 4, 0, 6, 0]
#arr = [1, 0, 1, 1, 2, 3]
arr.sort()

print(babyjin())