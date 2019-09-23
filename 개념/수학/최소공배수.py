arr = [2,6,8,14]
ans = 0
while arr:
    arr.sort()
    # print(arr)
    num1 = arr.pop(0)
    num2 = arr.pop(0)
    num = num2
    # print(num, num1)
    while num:
        if num % num1 == 0 and num % num2 == 0:
            if arr:
                arr.insert(0, num)
            break
        num += 1

    ans = num
print(num)