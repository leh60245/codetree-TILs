# n x n 격자
# 3명 이상이 한 팀
# 모든 사람들은 자신 앞 사람 허리 잡음.
#   용어
#   - 머리사람: 맨 앞사람
#   - 꼬리사람: 맨 뒤 사람
# 각 팀은 주어진 이동선을 따라서만 이동.
# 각 팀의 이동선은 끝이 이어져 있음
# 각 팀의 이동선은 서로 겹치지 않음

# 하나의 라운드 시작. (각 라운드는 별도로 진행)
# [1] 사람들 이동
# 머리 사람을 따라서 한 칸 이동

# [2]
# 공이 정해진 선을 따라 던져짐
#   1 Round에는 1행 RIGHT
#   2 Round에는 2행
#   ...
#   n Round에는 n행
#   n+1 Round에는 1열 UP
#   ...
#   2n+1 ~ 3n Round는 n행 -> 1행 순으로 LEFT에서 던져짐
#   4N Round 부터는 다시 처음부터 시작

# [3]
# 공이 던져지는 경우 해당 선에 사람이 있으면, 최초에 만나는 사람"만"이 공을 얻어 점수를 얻는다.
# 점수는 해당 사람이 '머리사람'을 시작으로 팀 내 k 번째 사람이라면, k의 제곱 만큼 점수를 얻는다.
# 아무도 못 받는다면 아무 점수도 획득 못한다.
#   공을 획득한 팀은 머리사람과 꼬리 사람이 바뀐다. 즉 방향이 바뀐다.

# [4]
# 각 팀이 획득한 점수의 총 합을 구하오
# 0은 빈칸, 1은 머리사람, 2는 나머지, 3은 꼬리사람, 4는 이동선
# 이동선의 각 칸은 반드시 2개의 인접한 칸만 존재, 하나의 이동 선에는 하나의 팀만이 존재.

import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
ARR = []  # 원본 그림
root_arr = [[0] * N for _ in range(N)]  # 여기는 이동 경로만 그려놓음
for _ in range(N):
    in_list = list(map(int, input().split()))
    ARR.append(in_list)
    new_list = list()
    for i in in_list:
        if i > 0:
            new_list.append(1)
        else:
            new_list.append(0)


def in_box(i, j):
    return 0 <= i < N and 0 <= j < N


def find_teams():
    teams = []
    team_idx = 1
    for i in range(N):
        for j in range(N):
            # 머리사람 찾음
            if ARR[i][j] == 1:
                team = bfs(i, j, team_idx)
                teams.append(team)
                team_idx += 1
    return teams


def bfs(i, j, team_idx):
    q = deque()
    global root_arr

    q.append((i, j))
    root_arr[i][j] = team_idx

    path = [(i, j)]
    last_point = None
    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if not in_box(ni, nj) or root_arr[ni][nj] or ARR[ni][nj] == 0:
                continue
            if ARR[ni][nj] == 2:
                q.append((ni, nj))
                root_arr[ni][nj] = team_idx
                path.append((ni, nj))
            elif ARR[ni][nj] == 3:
                last_point = ni, nj
                root_arr[ni][nj] = team_idx
    path.append(last_point)

    return path


team_list = find_teams()


def mv_teams(teams):
    global ARR
    for team_idx in range(M):
        head_i, head_j = teams[team_idx][0]
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = head_i + di, head_j + dj
            if not in_box(ni, nj) or ARR[ni][nj] == 0 or ARR[ni][nj] == 2:
                continue
            if ARR[ni][nj] == 4 or ARR[ni][nj] == 3:
                tail_i, tail_j = teams[team_idx][-1]
                ARR[tail_i][tail_j] = 4
                stail_i, stail_j = teams[team_idx][-2]
                ARR[stail_i][stail_j] = 3  # 새로운 꼬리
                ARR[head_i][head_j] = 2
                ARR[ni][nj] = 1  # 새로운 헤드

                teams[team_idx] = [(ni, nj)] + teams[team_idx][:-1]
                break
    return teams

answer = 0
for round in range(K):
    # [1] 사람들 이동
    # 머리 사람을 따라서 한 칸 이동
    team_list = mv_teams(team_list)

    # [2]
    # 공이 정해진 선을 따라 던져짐
    #   1 Round에는 1행 RIGHT
    #   2 Round에는 2행
    #   ...
    #   n Round에는 n행
    #   n+1 Round에는 1열 UP
    #   ...
    #   2n+1 ~ 3n Round는 n행 -> 1행 순으로 LEFT에서 던져짐
    #   4N Round 부터는 다시 처음부터 시작

    # 0:>, 1:^, 2:<, 3:아래로
    boll_dist, boll_line = (round // N) % 4, round % N
    if boll_dist >= 2:
        boll_line = N - boll_line - 1

    # [3]
    # 공이 던져지는 경우 해당 선에 사람이 있으면, 최초에 만나는 사람"만"이 공을 얻어 점수를 얻는다.
    # 점수는 해당 사람이 '머리사람'을 시작으로 팀 내 k 번째 사람이라면, k의 제곱 만큼 점수를 얻는다.
    # 아무도 못 받는다면 아무 점수도 획득 못한다.
    #   공을 획득한 팀은 머리사람과 꼬리 사람이 바뀐다. 즉 방향이 바뀐다.
    turn_point = 0
    find_team = False
    if boll_dist == 0:
        for j in range(N):
            if ARR[boll_line][j] == 1 or ARR[boll_line][j] == 2 or ARR[boll_line][j] == 3:
                for team_idx in range(M):
                    k = 1
                    for pi, pj in team_list[team_idx]:
                        if (boll_line, j) == (pi, pj):
                            find_team = True
                            turn_point += k ** 2

                            h_i, h_j = team_list[team_idx][0]
                            t_i, t_j = team_list[team_idx][-1]
                            ARR[t_i][t_j] = 1
                            ARR[h_i][h_j] = 3
                            team_list[team_idx].reverse()
                            break
                        k += 1
                    if find_team:
                        break
            if find_team:
                break
    elif boll_dist == 1:    # 위로 향하는 바람 i=N-1...0, 왼쪽 열(0)번부터 N-1번 열까지
        for i in range(N-1,-1,-1):
            if ARR[i][boll_line] == 1 or ARR[i][boll_line] == 2 or ARR[i][boll_line] == 3:
                for team_idx in range(M):
                    k = 1
                    for pi, pj in team_list[team_idx]:
                        if (i, boll_line) == (pi, pj):
                            find_team = True
                            turn_point += k ** 2

                            h_i, h_j = team_list[team_idx][0]
                            t_i, t_j = team_list[team_idx][-1]
                            ARR[t_i][t_j] = 1
                            ARR[h_i][h_j] = 3
                            team_list[team_idx].reverse()
                            break
                        k += 1
                    if find_team:
                        break
            if find_team:
                break
    elif boll_dist == 2:  # <, 아래 행(N-1)부터 0번 행까지
        for j in range(N-1, -1, -1):
            if ARR[boll_line][j] == 1 or ARR[boll_line][j] == 2 or ARR[boll_line][j] == 3:
                for team_idx in range(M):
                    k = 1
                    for pi, pj in team_list[team_idx]:
                        if (boll_line, j) == (pi, pj):
                            find_team = True
                            turn_point += k ** 2

                            h_i, h_j = team_list[team_idx][0]
                            t_i, t_j = team_list[team_idx][-1]
                            ARR[t_i][t_j] = 1
                            ARR[h_i][h_j] = 3
                            team_list[team_idx].reverse()
                            break
                        k += 1
                    if find_team:
                        break
            if find_team:
                break
    else:  # 아래로 향하는 바람 0...N-1, 오른쪽 열(N-1)번부터 0번 열까지
        for i in range(N):
            if ARR[i][boll_line] == 1 or ARR[i][boll_line] == 2 or ARR[i][boll_line] == 3:
                for team_idx in range(M):
                    k = 1
                    for pi, pj in team_list[team_idx]:
                        if (i, boll_line) == (pi, pj):
                            find_team = True
                            turn_point += k ** 2

                            h_i, h_j = team_list[team_idx][0]
                            t_i, t_j = team_list[team_idx][-1]
                            ARR[t_i][t_j] = 1
                            ARR[h_i][h_j] = 3
                            team_list[team_idx].reverse()
                            break
                        k += 1
                    if find_team:
                        break
            if find_team:
                break
    answer += turn_point

print(answer)