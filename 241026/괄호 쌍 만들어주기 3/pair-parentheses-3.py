arr = list(input())

cnt = 0
for i in range(len(arr)-1):
    if arr[i] == ")":
        continue
    for j in range(i+1, len(arr)):
        if arr[j] == ")":
            cnt += 1
print(cnt)