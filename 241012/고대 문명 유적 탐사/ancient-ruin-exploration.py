# 격자 크기 5x5
# 유물 조각 종류는 7가지. 1~7로 표기

# [1] 탐사 진행
# [1-1] 3x3 격자 선택
# 선택된 격자는 시계방향 90, 180, 270도 무조건 회전
# [1-2] 회전 목표
#   가능한 회전 방법중
#   1) 유물 1차 획득 가치를 최대화
#   2) 회전 각도 작은 방법
#   3) 열이 가장 작은 구간
#   4) 행이 가장 작은 구간

# [2] 유물 획득
# [2-1] 유물 1차 획득
# 상하좌우 인접한 같은 종류의 조각들이 3개 이상 연결된 경우, 조각이 모여 유물이 되고 사라진다.
# 유물의 가치는 '개수'와 같다.
# 유적지 벽면에는 1~7 사이 숫자 M개가 적혀 있다. 이들은 조각이 사리지고 새로 생기는 조각의 정보다.
# 벽면 순서대로 새로운 조각이 생성.
#   1) 열 번호가 작은 순서
#   2) 행 번호가 큰 순서
# 생겨날 조각의 수가 부족한 경우는 없다.
# 사용한 숫자는 못쓰고, 남은 순서대로 진행
# [2-2] 유물 연쇄 획득 2차 ~ 이후 획득들
# 마찬가지로 인접한 조각들이 유물이 되고 사라지고 생성된다.
# turn ending point: 더 이상 조각이 3개 이상 연결되지 않아 유물이 될 수 없을 때가지 반복한다.

# [3] 탐사 반복
# [1] 탐사 진행 부터 [2] 유물 획득 전체 과정을 1턴
# 총 K번 턴에 걸침
# 각 턴마다 획득한 유물의 가치 총합을 출력해야 한다.
# Game ending point: K 이전이지만, [1] 탐사 진행 과정에서 어떠한 방법을 사용해도 유물을 획득할 수 없다면 모든 탐사 종료.
#   이 경우 얻을 수 있는 유물이 존재하지 않으므로, 종료되는 턴에 아무 값도 출력하지 않는다.

import sys
from collections import deque

input = sys.stdin.readline
K, M = map(int, input().split())
ARR = []
for _ in range(5):
    ARR.append(list(map(int, input().split())))
wall_info = deque(list(map(int, input().split())))


def in_box(i, j):
    return 0 <= i < 5 and 0 <= j < 5


def rotate(si, sj, cnt, arr):
    rotate_arr = [[0] * 5 for _ in range(5)]
    for i in range(si, si + 3):
        for j in range(sj, sj + 3):
            oi, oj = i - si, j - sj
            for _ in range(cnt):  # 1, 2, 3
                oi, oj = oj, 2 - oi
            ni, nj = oi + si, oj + sj
            rotate_arr[ni][nj] = arr[i][j]

    for i in range(5):
        for j in range(5):
            if rotate_arr[i][j] == 0:
                rotate_arr[i][j] = arr[i][j]

    return rotate_arr


def bfs(si, sj, arr, visited):
    q = deque()
    cp_v = [i[:] for i in visited]
    point = 0
    ty = arr[si][sj]

    q.append((si, sj))
    cp_v[si][sj] = 1
    point += 1

    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if not in_box(ni, nj) or cp_v[ni][nj] or arr[ni][nj] != ty:
                continue
            q.append((ni, nj))
            cp_v[ni][nj] = 1
            point += 1

    if point >= 3:
        return point, cp_v
    else:
        return 0, visited


def to_zero(arr, v):
    # arr에서 제거
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                arr[i][j] = 0
    return arr


def fill_zero(arr):
    # 채워 넣기
    # 유적지 벽면에는 1~7 사이 숫자 M개가 적혀 있다. 이들은 조각이 사리지고 새로 생기는 조각의 정보다.
    # 벽면 순서대로 새로운 조각이 생성.
    #   1) 열 번호가 작은 순서
    #   2) 행 번호가 큰 순서
    # 생겨날 조각의 수가 부족한 경우는 없다.
    # 사용한 숫자는 못쓰고, 남은 순서대로 진행
    for j in range(5):
        for i in range(4, -1, -1):
            if arr[i][j] == 0:
                arr[i][j] = wall_info.popleft()
    return arr


def get_point(arr):
    # 유물 얻기
    point = 0
    v = [[0] * 5 for _ in range(5)]  # 방문한 기록 누적 시키기
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 0:
                continue
            p, v = bfs(i, j, arr, v)
            point += p

    return point, v


def get_first_point(arr):
    # [1-1] 3x3 격자 선택
    # 선택된 격자는 시계방향 90, 180, 270도 무조건 회전
    # [1-2] 회전 목표
    #   가능한 회전 방법중
    #   1) 유물 1차 획득 가치를 최대화
    #   2) 회전 각도 작은 방법
    #   3) 열이 가장 작은 구간
    #   4) 행이 가장 작은 구간
    max_point = 0
    save_arr = None
    save_visited = None
    for rotate_cnt in range(1, 4):
        for rj in range(3):
            for ri in range(3):
                new_arr = rotate(ri, rj, rotate_cnt, arr)
                p, v = get_point(new_arr)
                if max_point < p:
                    max_point = p
                    save_arr = new_arr
                    save_visited = v
    if max_point == 0:
        return 0, arr

    save_arr = to_zero(save_arr, save_visited)
    save_arr = fill_zero(save_arr)
    return max_point, save_arr


for _ in range(K):
    turn_point = 0

    # [2-1] 유물 1차 획득
    first_point, ARR = get_first_point(ARR)
    turn_point += first_point
    # Game ending point
    if first_point == 0:
        break

    # [2-2] 유물 연쇄 획득
    while True:
        after_point, after_visited = get_point(ARR)
        turn_point += after_point
        # Turn Ending point
        if after_point == 0:
            break
        ARR = to_zero(ARR, after_visited)
        ARR = fill_zero(ARR)

    # 총 얻은 값 표출
    print(turn_point, end=" ")