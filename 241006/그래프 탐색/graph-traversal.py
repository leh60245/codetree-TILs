import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [
    [0] * n for _ in range(n)
]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1
visited = [False] * n
ans = 0

def mv(idx):
    global ans
    for i in range(n):
        if not visited[i] and graph[idx][i] :
            visited[i] = True
            ans += 1
            mv(i)



visited[0] = True
mv(0)
print(ans)