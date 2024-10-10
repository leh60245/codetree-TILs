# P번까지 산타
# N N 격자. 위치는 r, c 형태, 좌상단 1, 1
# 총 M턴

import sys
from collections import deque

imput = sys.stdin.readline
# N: 격자 크기, M: , P: 산타 수, C: , D:
N, M, P, C, D = map(int, input().split())
# 루돌프 초기 위치 인덱스
RR, RC = map(int, input().split())
RR, RC = RR - 1, RC - 1
# 산타 위치 인덱스 + 기절 턴(0:멀쩡) + 생존(1:생존, 0:탈락) +점수
santa_info = {}
for _ in range(P):
    pn, sr, sc = map(int, input().split())
    santa_info[pn] = (sr - 1, sc - 1, 0, 1, 0)

rodolf_direction_list = {
    0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)
}

save_score_list = {}


def cal_dis(r1, c1, r2, c2):
    return pow((r1 - r2), 2) + pow((c1 - c2), 2)


def in_box(i, j):
    return 0 <= i < N and 0 <= j < N


def mv_rodolf(rodolf_i, rodolf_j):
    # [루돌프의 움직임]
    # 가까운 산타를 향해 1칸 돌진
    # 단, 게임에서 탈락하지 않은 산타 중 '가장 가까운 산타'를 선택.
    # 가까운 산타가 2명 이상이라면, 'r 좌표가 큰 산타로 돌진'. 다음은 'c'좌표
    # 루돌프는 상하좌우, 대각선 포함한 8방향. 가장 우선순위 높은 산타로 가장 가까워지는 한 칸 돌진
    min_distant_result = pow(N, 2) * 2
    near_santa_index = 0
    for santa_index in sorted(santa_info.keys()):
        si, sj, _, sv, _ = santa_info[santa_index]
        if sv == 0:
            continue
        distant = cal_dis(rodolf_i, rodolf_j, si, sj)
        # 더 짧다면 변경
        if min_distant_result > distant:
            min_distant_result = distant
            near_santa_index = santa_index
        # 거리가 동일하면 조건에 맞는거 선택
        elif min_distant_result == distant:
            # 거리가 같다면 더 조건에 맞는 것을 골라야 한다.
            # santa_index vs near_santa_index
            before_i, before_j, _, _, _ = santa_info[near_santa_index]
            if si > before_i:
                near_santa_index = santa_index
            elif si == before_i and sj > before_j:
                near_santa_index = santa_index

    # 거리가 가까워지는 방향으로 한칸 이동하기.
    target_i, target_j, _, _, _ = santa_info[near_santa_index]
    # print("target santa index:", near_santa_index, ". x y:", target_i, target_j)
    min_lenght = pow(N, 2) * 2
    next_rodolf_i, next_rodolf_j = None, None
    direction_index = -1
    for dd in range(8):
        di, dj = rodolf_direction_list[dd]
        ni, nj = rodolf_i + di, rodolf_j + dj
        result_d = cal_dis(ni, nj, target_i, target_j)  # 다음 방향 위치와 타겟 산타 거리 계산
        if min_lenght > result_d:
            min_lenght = result_d
            next_rodolf_i, next_rodolf_j = ni, nj
            direction_index = dd

    return next_rodolf_i, next_rodolf_j, direction_index


def mv_santas(santa_idx, turn_number):
    # [2] 산타들, 1번부터 P번까지 순차적으로 움직임
    global santa_info
    santa_i, santa_j, santa_turn, santa_save, santa_score = santa_info[santa_idx]
    # 이번 턴에 깨어남 -> 정상
    if santa_turn == turn_number:
        santa_turn = 0

    # 루돌프로 가까워지는 방향으로 1칸 이동
    # 단, 다른 산타가 있다면 움직일 수 없음, 게임 밖도 안됨
    # 움직일 수 있는 칸이 없다면 움직이지 않음
    # 움직일 수 있는 칸이 있더라도 루돌프와 가까워질 수 있는 방법이 없다면 움직이지 않음
    # 상하좌우 4 방향 중 한 곳. 우선순위도 상하좌우

    # 루돌프로 한 칸 이동
    min_lenght = cal_dis(santa_i, santa_j, RR, RC)  # 지금 루돌프와의 거리
    next_santa_i, next_santa_j = santa_i, santa_j
    drt_index = None
    for drt in range(4):
        drt = drt * 2
        di, dj = rodolf_direction_list[drt]
        ni, nj = santa_i + di, santa_j + dj  # 움직인 위치
        # 1. 상자 안
        if not in_box(ni, nj):
            continue
        result_d = cal_dis(ni, nj, RR, RC)
        # 거리가 짧아지지 않는다면, 볼 필요 없음,
        if result_d >= min_lenght:
            continue
        # 3. 움직인 위치에 산타가 있는지 확인한다.
        is_there_santa = False
        for is_santa in sorted(santa_info.keys()):
            is_i, is_j, _, is_save, _ = santa_info[is_santa]
            if is_santa == santa_idx or is_save == 0:
                continue
            # 산타가 자리에 있다면 그 자리는 건너 뛴다.
            if (ni, nj) == (is_i, is_j):
                is_there_santa = True
                break
        if is_there_santa:
            continue
        # 움직인 위치에 산타도 없고, 거리도 짧아진다면, 갱신
        min_lenght = result_d
        next_santa_i, next_santa_j = ni, nj
        drt_index = drt

    # 위 for문을 통해 산타의 다음 자리가 정해졌다.
    santa_info[santa_idx] = next_santa_i, next_santa_j, santa_turn, santa_save, santa_score

    return drt_index


def rodolf_to_santa(santa_idx, direction_num, turn_number, power):
    # [충돌]
    # 산타는 C 만큼 점수를 얻고, 동시에 루돌프가 이동해온 방향으로 C칸 밀린다.
    # 밀려나는 것은 포물선 모양을 그리기에 이동하는 도중 충돌이 없고, 원하는 위치에 도달한다.
    # 게임판 밖이라면 산타는 게임에서 탈락
    # 밀려난 칸에 다른 산타가 있다면 -> 상호작용 발생
    # [기절]
    # 산타는 루돌프와 충돌 후 '기절'을 한다.
    # 지금 턴이 k라면 (k+1)번 까지 기절하여 (k+2)부터 정상
    # 기절한 산타는 움직일 수 없다. 단, [충돌]이나 [상호작용]으로 밀려날 수 있다.
    # 기절한 산타를 돌진 대상으로 선택할 수 있다.
    global santa_info
    santa_i, santa_j, santa_turn, santa_save, santa_score = santa_info[santa_idx]
    santa_score += power
    di, dj = rodolf_direction_list[direction_num]
    santa_i, santa_j = santa_i + di * power, santa_j + dj * power
    santa_turn = turn_number + 2  # 깨어나는 턴
    if not in_box(santa_i, santa_j):
        # print("Died santa index:", santa_idx)
        santa_info[santa_idx] = santa_i, santa_j, santa_turn, 0, santa_score
        return
    santa_info[santa_idx] = santa_i, santa_j, santa_turn, santa_save, santa_score

    # [상호작용] 산타끼리
    # 밀려나 착지한 '칸에서만'(즉 칸 하나에서만) 상호작용 발생
    # 기존에 있던 다른 산타는 '1칸' '해당 방향'으로 밀린다.
    # 그 옆에 산타가 있다면 연쇄적으로 '1칸씩' 밀리는 것을 반복.
    # 게임판 밖으로 밀린 산타는 게임에서 탈락

    # 산타를 계속 찾아야 하므로 while 문을 돌림
    arrive_i, arrive_j = santa_i, santa_j  # 밀려난 칸 위치
    while True:
        stop_find_next_santa = True
        for next_santa_index in sorted(santa_info.keys()):
            # 나는 제외
            if next_santa_index == santa_idx:
                continue
            nsi, nsj, nsk, ns_save, ns_score = santa_info[next_santa_index]
            # 밀려난 칸에 산타가 있다면,
            if ns_save == 0:
                continue
            if (nsi, nsj) == (arrive_i, arrive_j):
                # print("crush santa: ", santa_idx, "->", next_santa_index)
                # 찾은 산타는 해당 방향으로 1칸 이동 함
                nsi, nsj = nsi + di, nsj + dj
                # print("santa", next_santa_index, "go to", nsi, nsj)
                # 이동을 한 곳이 장소 안이라면, 위치를 수정하고 다음 산타를 찾음
                if in_box(nsi, nsj):
                    santa_idx = next_santa_index
                    arrive_i, arrive_j = nsi, nsj
                    santa_info[next_santa_index] = nsi, nsj, nsk, ns_save, ns_score
                    stop_find_next_santa = False
                # 이동한 공간이 장소 밖이라면, 탈락 시키고 산타를 그만 찾음
                else:
                    # print("Died santa index:", next_santa_index)
                    santa_info[next_santa_index] = nsi, nsj, nsk, 0, ns_score
                # 밀려난 칸에 산타를 찾으면 더 이상 다른 산타는 찾을 필요가 없다.
                break

        # 더 이상 다음 산타가 없다면 나간다.
        if stop_find_next_santa:
            break

    return


def print_arr():
    arr = [[0] * N for _ in range(N)]
    arr[RR][RC] = -1
    for santa_index in sorted(santa_info.keys()):
        santa_i, santa_j, _, santa_save, _ = santa_info[santa_index]
        if santa_save == 0:
            continue
        arr[santa_i][santa_j] = santa_index
    for ari in arr:
        print(*ari)


# turn
for turn_number in range(M):
    # print("\nturn:", turn_number)
    # print_arr()

    # [1] 루돌프 이동
    RR, RC, rodolf_direction = mv_rodolf(RR, RC)
    # print("next rodolf index:", RR, RC)
    # print_arr()

    # [루돌프의 이동으로 산타의 충돌과 상호작용, 기절]
    for santa_index in sorted(santa_info.keys()):
        santa_i, santa_j, _, santa_save, _ = santa_info[santa_index]
        if santa_save == 0:
            continue
        if (RR, RC) == (santa_i, santa_j):
            # print("rodolf crush santa index:", santa_index)
            rodolf_to_santa(santa_index, rodolf_direction, turn_number, C)
            # print_arr()

    # [2] 산타 순차적 이동
    for santa_index in sorted(santa_info.keys()):
        _, _, santa_k, santa_save, _ = santa_info[santa_index]
        # 탈락하거나 기절한 산타는 스스로 움직일 수 없다.
        if santa_save == 0 or 0 < turn_number < santa_k:
            continue
        # 산타 다음 좌표로 업데이트
        santa_direction = mv_santas(santa_index, turn_number)
        # print("index", santa_index, ". next direction:", santa_direction)
        # print_arr()
        # [산타의 이동으로 루돌프와 충돌 후 산타의 기절 및 상호작용]
        if (santa_info[santa_index][0], santa_info[santa_index][1]) == (RR, RC):
            # print("santa crush index:", RR, RC)
            # print_arr()
            rodolf_to_santa(santa_index, (santa_direction + 4) % 8, turn_number, D)

    # 매턴 이후 탈락하지 않은 산타들에게는 1점을 추가로 부여한다.
    # P명 산타 모두 게임에서 탈락하면, 게임은 종료된다.
    not_save_cnt = 0
    for santa_index in sorted(santa_info.keys()):
        i, j, k, san_save, san_score = santa_info[santa_index]
        if san_save == 0:
            continue
        san_score += 1
        santa_info[santa_index] = i, j, k, san_save, san_score
    else:
        not_save_cnt += 1
    # print("turn end")
    # print_arr()
    if not_save_cnt == P:
        # print("game over")
        break

for santa_index in sorted(santa_info.keys()):
    print(santa_info[santa_index][4], end=" ")