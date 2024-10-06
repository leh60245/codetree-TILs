import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [
    [False] * m for _ in range(n)
]
dxs, dys = [1, 0], [0, 1]

def in_box(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    return in_box(x, y) and arr[x][y] == 1

ans = 0
def dfs(x, y):
    global ans
    print(x, y)
    if x == n-1 and y == m-1:
        ans = 1
        return
    for i in range(2):
        dx, dy = x + dxs[i], y + dys[i]
        if can_go(dx, dy):
            visited[dx][dy] = True
            dfs(dx, dy)

dfs(0,0)
print(ans)