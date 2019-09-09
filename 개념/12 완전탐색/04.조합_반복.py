arr = "ABCDE"
N = len(arr)

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            print(arr[i], arr[j], arr[k])
