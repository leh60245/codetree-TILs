from collections import deque

def in_box(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def bfs(i, j, n, m, arr):
    q = deque()
    v = [[0] * m for _ in range(n)]

    q.append((i, j))
    v[i][j] = 1

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (n - 1, m - 1):
            return 1
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if not in_box(ni, nj, n, m) or v[ni][nj] or arr[ni][nj] == 0:
                continue
            q.append((ni, nj))
            v[ni][nj] = 1

    return 0


def main():
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    print(bfs(0, 0, n, m, arr))

if  __name__ == "__main__":
    main()