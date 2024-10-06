import sys

input = sys.stdin.readline
k, n = map(int, input().split())
arr = [i for i in range(1, k + 1)]
visited = [0] * n


def con(cnt, sm, sm_cnt):  # cnt: 위치, sm: 이전 값, sm_cnt 중복된 횟수
    if sm_cnt >= 3:
        return
    if cnt == n and sm_cnt < 3:
        print(*visited)
        return
    for i in range(1, k + 1):
        visited[cnt] = i
        if sm == i:
            con(cnt + 1, i, sm_cnt + 1)
        else:
            con(cnt + 1, i, 1)
        visited[cnt] = 0

con(0, 0, 0)