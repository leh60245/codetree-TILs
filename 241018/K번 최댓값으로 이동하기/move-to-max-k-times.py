from collections import deque

N, K = map(int, input().split())
ARR = []
for _ in range(N):
    ARR.append(list(map(int, input().split())))
R, C = map(int, input().split())
R, C = R - 1, C - 1

def in_box(i, j):
    return 0 <= i < N and 0 <= j < N

def bfs(si, sj):
    q = deque()
    v = [[0] * N for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1
    limit = ARR[si][sj]
    max_value = 0
    next_i, next_j = si, sj

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ni, nj = ci + di, cj + dj
            if not in_box(ni, nj) or v[ni][nj] or ARR[ni][nj] >= limit:
                continue
            q.append((ni, nj))
            v[ni][nj] = 1
            if max_value < ARR[ni][nj]:
                max_value = ARR[ni][nj]
                next_i, next_j = ni, nj
            elif max_value == ARR[ni][nj]:
                if (next_i, next_j) > (ni, nj):
                    next_i, next_j = ni, nj

    return next_i, next_j



next_r, next_c = None, None
for _ in range(K):
    next_r, next_c = bfs(R, C)
    if (next_r, next_c) == (R, C):
        break
    R, C = next_r, next_c

print(next_r + 1, next_c + 1)