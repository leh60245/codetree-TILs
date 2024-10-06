import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [
    [False] * n for _ in range(n)
]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
ans = []


def in_box(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y):
    return in_box(x, y) and not visited[x][y]


def dfs(x, y):
    global cnt
    # print(x, y)
    for i in range(4):
        dx, dy = x + dxs[i], y + dys[i]
        if can_go(dx, dy) and arr[x][y] == arr[dx][dy] :
            visited[dx][dy] = True
            cnt += 1
            dfs(dx, dy)

block_cnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            cnt = 1
            visited[i][j] = True
            dfs(i, j)
            if cnt >= 4:
                block_cnt += 1
            ans.append(cnt)

print(block_cnt, max(ans))