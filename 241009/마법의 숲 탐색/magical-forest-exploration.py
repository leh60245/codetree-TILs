# 동 서 남에 벽, 북을 통해 들어올 수 있음
# 정령 K명. 골렘은 십자 모양 총 5칸. 골램 상하좌우 칸 중 한 칸은 골렘의 출구.
#   -> 골렘 탑승은 어떤 방향도 가능하지만, 내릴 때는 정해진 출구를 통해서만 내릴 수 있음
# i번째로 숲을 탐색하는 골램 gi는 숲 북쪽에서 시작. 골렘 중앙이 ci 열이 되도록 하는 위치에서 내려온다.
# 초기 골렘의 출구는 di의 방향에 위치

import sys
from collections import deque


# 골렘 중앙 좌표의 박스 안 위치라 양 사이드 위치는 없음
def in_box(i, j):
    global R, C
    return 1 <= i < (R + 2) and 1 <= j < (C - 1)


def mv_golem(start_i, start_j, direction, arr):
    chk_list = {
        0: [(2, 0), (1, -1), (1, 1)],
        1: [(-1, -1), (0, -2), (1, -1), (1, -2), (2, -1)],
        2: [(-1, 1), (0, 2), (1, 1), (1, 2), (2, 1)]
    }
    ci, cj = start_i, start_j

    while True:
        can_move = False
        for chk_num, dd in enumerate([(1, 0), (1, -1), (1, 1)]):
            ni, nj = ci + dd[0], cj + dd[1]

            # 1. 중앙 위치기 박스 안에 있는지 확인
            if not in_box(ni, nj):
                continue

            # 2. 움직일 위치(초록색)에 다른 golem이 있는지 확인
            there_is_golem = False
            for chk_i, chk_j in chk_list[chk_num]:
                green_i, green_j = ci + chk_i, cj + chk_j
                if arr[green_i][green_j]:
                    there_is_golem = True
                    break
            if there_is_golem:
                continue

            # 3. 움직일 수 있다면 회전하고 움직이고 끝낸다.
            can_move = True
            ci, cj = ni, nj
            break
        # 더이상 움직일 수 없다면 나간다.
        if not can_move:
            break

    rotate = cj - start_j
    # print(rotate)
    rotate = (direction + rotate) % 4

    return ci, cj, rotate


def mv_twinkle(start_i, start_j, arr, g_info):
    q = deque()
    v = [[0] * C for _ in range(R + 3)]

    q.append((start_i, start_j))
    v[start_i][start_j] = 1

    max_deep = start_i
    # for arrr in arr:
    #     print(*arrr)
    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            # 박스 안, 방문 한 기록 없어야 함, 골램이 있어야 함
            if 0 <= ni < (R + 3) and 0 <= nj < C and not v[ni][nj] and arr[ni][nj] > 0:
                c_num = arr[ci][cj]
                n_num = arr[ni][nj]
                # 지금 골램과 다음 골램이 다르다면
                if c_num != n_num:
                    # 지금 위치가 입구가 되어야 한다.
                    if (ci, cj) == g_info[c_num]:
                        q.append((ni, nj))
                        v[ni][nj] = 1
                        max_deep = max(max_deep, ni)
                else:
                    q.append((ni, nj))
                    v[ni][nj] = 1
                    max_deep = max(max_deep, ni)

    # print(max_deep)
    return max_deep


input = sys.stdin.readline
R, C, K = map(int, input().split())
arr = [[0] * C for _ in range(R + 3)]  # 세로 R+3, 가로 C 크기의 숲
output_info = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # (북:0, 동:1, 남:2, 서:3)
golem_info = {}  # 골렘의 번호 : (골렘의 출구 위치 인덱스)
ans = 0  # 정령의 최종 위치의 '행'번호
for turn_number in range(1, K + 1):  # 골렘마다 번호 메김
    # [1] 골램 움직임
    c, d = map(int, input().split())  # 출발 열 c와 출구 방향 d 정보

    s_i, s_j = 1, c - 1  # 첫 골렘 중앙의 좌표. 무조건 1번 인덱스 행과 c-1 인덱스 열에서 시작
    # print("start golem info:", s_j, d)
    next_i, next_j, next_direction = mv_golem(s_i, s_j, d, arr)
    # 만약 숲에 들어가지 않았다면 멈추고 모든 골램들을 빼낸다.
    if next_i < 4:
        arr = [[0] * C for _ in range(R + 3)]  # 숲 초기화
        continue
    # 숲에 골램을 위치 시키고, 골램의 방향 정보를 기록한다.
    for di, dj in [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]:
        arr[next_i + di][next_j + dj] = turn_number
    output_i, output_j = next_i + output_info[next_direction][0], next_j + output_info[next_direction][1]
    golem_info[turn_number] = (output_i, output_j)
    # print("end   golem info:", next_i, next_j, output_i, output_j)
    # [2] 요정 움직임
    twinkle_i, twinkle_j = next_i, next_j  # 지금 위치
    # 지금 위치 정보와 함께 골램의 번호와 골램의 출구 정보를 제공해줘야 한다.
    twinkle_max_deep = mv_twinkle(twinkle_i, twinkle_j, arr, golem_info)
    # print("end twinkle:", twinkle_max_deep)
    ans += twinkle_max_deep - 2  # 인덱스 - 2  행이 3개 추가 되었기에
    # print(ans)

print(ans)