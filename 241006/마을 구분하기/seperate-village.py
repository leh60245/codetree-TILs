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
    return in_box(x, y) and arr[x][y] == 1 and not visited[x][y]


def dfs(x, y):
    global cnt
    # print(x, y)
    for i in range(4):
        dx, dy = x + dxs[i], y + dys[i]
        if can_go(dx, dy):
            visited[dx][dy] = True
            cnt += 1
            dfs(dx, dy)


for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            cnt = 1
            visited[i][j] = True
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)