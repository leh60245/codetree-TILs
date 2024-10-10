import sys
from collections import deque

input = sys.stdin.readline
# NxM 격자, K 턴
N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

last_attack_turn_history = [[0] * M for _ in range(N)]  # 마지막으로 공격한 turn 번호 저장


def chk_attacker():
    min_dmg = 5001
    i, j = 0, 0
    for ci in range(N):
        for cj in range(M):
            # 부서진 포탑은 지나감
            c_dmg = arr[ci][cj]
            if c_dmg == 0:
                continue

            # if c_dmg < min_dmg:
            #     min_dmg = c_dmg
            #     i, j = ci, cj
            # elif c_dmg == min_dmg:
            #     if last_attack_turn_history[ci][cj] > last_attack_turn_history[i][j]:
            #         ci, cj = i, j
            #     elif last_attack_turn_history[ci][cj] == last_attack_turn_history[i][j]:
            #         if ci + cj > i + j:
            #             ci, cj = i, j
            #         elif ci + cj == i + j:
            #             if cj > j:
            #                 ci, cj = i, j

            # (피해량, 공격 시간, 행+열 합, 열 값)으로 튜플을 비교
            if (c_dmg, last_attack_turn_history[i][j], i + j, j) < (
                    min_dmg, last_attack_turn_history[ci][cj], ci + cj, cj):
                min_dmg = c_dmg
                i, j = ci, cj

    return i, j


def chk_target(attacker_i, attacker_j):
    max_dmg = 0
    i, j = 0, 0
    for ci in range(N):
        for cj in range(M):
            # 부서진 포탑과 공격자는 지나감
            c_dmg = arr[ci][cj]
            if c_dmg == 0 or (attacker_i, attacker_j) == (ci, cj):
                continue
            # (피해량, 공격 시간, 행+열 합, 열 값)으로 튜플을 비교
            if (c_dmg, last_attack_turn_history[i][j], i + j, j) > (
                    max_dmg, last_attack_turn_history[ci][cj], ci + cj, cj):
                max_dmg = c_dmg
                i, j = ci, cj

    return i, j


def lizer(attacker_i, attacker_j, target_i, target_j):
    q = deque()
    v = [[0] * M for _ in range(N)]

    q.append((attacker_i, attacker_j))
    v[attacker_i][attacker_j] = 1

    path = {(attacker_i, attacker_j): None}  # (i, j) : (ni, nj)

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (target_i, target_j):
            # 여기에 이전 경로 추적하는 것을 작성해야 한다.
            path_list = []
            back_start = (target_i, target_j)
            while back_start:
                path_list.append(back_start)
                back_start = path[back_start]

            return path_list[:-1]
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = (ci + di) % N, (cj + dj) % M  # N x M 격자 벽은 상관 없음
            # 단, 부서진 포탑이나 지나간 경로면 돌아감
            if arr[ni][nj] == 0 or v[ni][nj]:
                continue
            q.append((ni, nj))
            v[ni][nj] = 1
            path[(ni, nj)] = (ci, cj)  # 경로 저장

    return []


def boom(attacker_i, attacker_j, target_i, target_j):
    around = [(target_i, target_j)]
    for di, dj in [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
        ni, nj = (target_i + di) % N, (target_j + dj) % M
        if arr[ni][nj] == 0 or (ni, nj) == (attacker_i, attacker_j):
            continue
        around.append((ni, nj))

    return around


for turn_number in range(1, K + 1):
    # [0] 모든 포탑이 건사한지 확인. 만약 하나만 1이라면 끝
    alive_cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                alive_cnt += 1
    if alive_cnt == 1:  ######## 왠지 1 이하일 것 같아 이렇게 함
        break

    action_in_turn = [[0] * M for _ in range(N)]  # 이번 턴에 활동을 했는지 확인
    # [1] 공격자 선정
    attacker_i, attacker_j = chk_attacker()
    arr[attacker_i][attacker_j] += N + M
    last_attack_turn_history[attacker_i][attacker_j] = turn_number
    action_in_turn[attacker_i][attacker_j] = 1  # 기록 저장

    # [2] 공격자의 공격
    # [2-1] target 선정
    target_i, target_j = chk_target(attacker_i, attacker_j)
    # [2-2] 공격 경로 및 범위 지정
    attack_path = lizer(attacker_i, attacker_j, target_i, target_j)
    if not attack_path:
        attack_path = boom(attacker_i, attacker_j, target_i, target_j)

    # [3] 포탑 부서짐. 공격 대상과 경로상의 포탑의 공격력 깎음
    for ti, tj in attack_path:
        if arr[ti][tj] == 0:
            continue
        if (ti, tj) == (target_i, target_j):
            arr[ti][tj] = max(arr[ti][tj] - arr[attacker_i][attacker_j], 0)
        else:
            arr[ti][tj] = max(arr[ti][tj] - (arr[attacker_i][attacker_j] // 2), 0)
        action_in_turn[ti][tj] = 1

    # [4] 포탑 정비 +1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                continue
            # 공격 관련 대상도 지나감
            if action_in_turn[i][j]:
                continue
            arr[i][j] += 1

# [final] 남은 포탑 중 가장 강력크한 포탑의 '공격력' 출력
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > ans:
            ans = arr[i][j]
print(ans)