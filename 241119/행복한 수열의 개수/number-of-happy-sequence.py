n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = 0
# 가로로
for i in range(n):
    tmp = arr[i][0]
    cnt = 1
    save_cnt = 1
    for j in range(1, n):
        if arr[i][j] == tmp:
            cnt += 1
        else:
            save_cnt = max(save_cnt, cnt)
            tmp = arr[i][j]
            cnt = 1
    save_cnt = max(save_cnt, cnt)
    if save_cnt >= m:
        ans += 1

# 세로로
for i in range(n):
    tmp = arr[0][i]
    cnt = 1
    save_cnt = 1
    for j in range(1, n):
        if arr[j][i] == tmp:
            cnt += 1
        else:
            save_cnt = max(save_cnt, cnt)
            tmp = arr[j][i]
            cnt = 1
    save_cnt = max(save_cnt, cnt)
    if save_cnt >= m:
        ans += 1

print(ans)