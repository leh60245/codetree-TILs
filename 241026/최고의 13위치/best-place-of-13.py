n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

max_cnt = 0
for i in range(n):
    for j in range(n-2):
        max_cnt = max(arr[i][j] + arr[i][j+1] + arr[i][j+2], max_cnt)
    if max_cnt == 3:
        break
print(max_cnt)