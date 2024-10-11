import sys
from collections import deque

input = sys.stdin.readline
# 격자 NxN, 사람 M명
N, M = map(int, input().split())

# 빈칸은 0, 베켐은 1, 벽은 2
# 도착한 편의점과 베켐은 사람들이 모두 움직이고 나면 벽이 된다.
# 그 전까지 사람은 빈칸, 베켐, 편의점을 지나다닐 수 있다.
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

shop_location = []  # 편의점 위치 저장 M개
for _ in range(M):
    shopi, shopj = map(int, input().split())
    shopi, shopj = shopi - 1, shopj - 1
    shop_location.append((shopi, shopj))
people_location = []  # 사람 위치 저장 (i, j) 총 M의 크기가 될 것임


def cal_len(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)  # 가야 하는 칸의 개수


def in_box(i, j):
    return 0 <= i < N and 0 <= j < N


def mv_people(people_cnt):
    people_cnt = min(people_cnt, M)  # 최대 M명을 넘지 못하도록 막음
    arrive_shop_loc = []  # 도착한 편의점을 벽으로 표시하기 위한 저장 장소
    for people_index in range(people_cnt):
        # 도착한 사람은 x
        if people_location[people_index] == shop_location[people_index]:
            continue
        # 이제 다음으로 움직일 위치를 정한다.
        people_location[people_index] = bfs_people(people_index)

        # 다음 최단거리 위치가 정해졌으면, 편의점에 도착했는지 확인한다.
        if people_location[people_index] == shop_location[people_index]:
            arrive_shop_loc.append(shop_location[people_index])

    # 사람들이 움직였으면, 이제 도착한 편의점은 벽이 된다.
    for i, j in arrive_shop_loc:
        arr[i][j] = 2

    return


def bfs_people(pi):
    start_i, start_j = people_location[pi]
    q = deque()
    v = [[0] * N for _ in range(N)]

    q.append((start_i, start_j))
    v[start_i][start_j] = 1

    path = {(start_i, start_j): None}
    while q:
        ci, cj = q.popleft()
        # 우리가 찾던 편의점이라면 경로 첫번째 움직임을 보내줌
        if (ci, cj) == shop_location[pi]:
            end_point = ci, cj
            path_list = list()
            path_list.append((ci, cj))
            while end_point:
                path_list.append(path[end_point])
                end_point = path[end_point]

            return path_list[-3]
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ni, nj = ci + di, cj + dj
            # 박스 외부 이거나 벽이면 안됌
            if not in_box(ni, nj) or arr[ni][nj] == 2 or v[ni][nj]:
                continue
            q.append((ni, nj))
            v[ni][nj] = 1
            path[(ni, nj)] = ci, cj

    return False


def start_in_becam(shop_index):
    shop_i, shop_j = shop_location[shop_index]
    q = deque()
    v = [[0] * N for _ in range(N)]

    q.append((shop_i, shop_j))
    v[shop_i][shop_j] = 1

    while q:
        ci, cj = q.popleft()
        # 우리가 찾던 베켐이라면 끝
        if arr[ci][cj] == 1:
            people_location.append((ci, cj))  # 사람이 처음 시작하는 위치 넣음
            arr[ci][cj] = 2  # 벽으로 변경
            return True
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ni, nj = ci + di, cj + dj
            # 박스 외부거나 방문한 지역이나 벽은 안됨
            if not in_box(ni, nj) or v[ni][nj] or arr[ni][nj] == 2:
                continue
            q.append((ni, nj))
            v[ni][nj] = 1

    return False


turn_number = 0  # 모두 도착까지 얼마나 걸리나 확인
while True:
    # [1] 격자 속 사람 이동
    mv_people(turn_number)

    # [2] 이동 후 사람들 확인하기
    # 못해도 M 턴 이후에 확인해야 한다.
    if turn_number >= M:
        end_game = True
        for chk_index in range(M):
            if people_location[chk_index] != shop_location[chk_index]:
                end_game = False
                break
        if end_game:
            break

    # [3] 다음 사람 배켐 선택
    if turn_number < M:
        start_in_becam(turn_number)

    # 다음 턴으로 가자
    turn_number += 1

print(turn_number + 1)