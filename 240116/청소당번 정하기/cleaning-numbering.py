n = int(input())
arr = [0,0,0]
for i in range(1,n+1):
    if i % 12 == 0:
        arr[2] += 1
    elif i % 3 == 0:
        arr[1] += 1
    elif i % 2 == 0:
        arr[0] += 1
print(*arr)