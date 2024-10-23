n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < n and 0 <= nj < n):
                continue
            if arr[ni][nj] == 1:
                cnt += 1

        if cnt >= 3:
            answer += 1

print(answer)