# n * n 격자. 각 격자에는 무기들이 있을 '수' 있음
# 처음엔 플레이어은 무기 없는 빈 격자에 위치시키고, 각 플레이어는 초기 능력을 가진다.
# <각 플레이어 초기 능ㄹ력치는 모두 다르다>
# 빨간색 배경 숫자는 총 = 공격력, 플레이어 = 초기 능력치.
# 노랑 배경 숫자는 플레이어의 번호


# 라운드 진행
# 1-1. 첫 번째 플레이어 부터 순차적으로
#       본인이 향하고 있는 방향대로 한 칸 이동한다.
#       해당 방향으로 나갈 때, 만약 격자를 벗어나는 경우 정반대 방향으로 방향을 바꾸어 1 만큼 이동한다.

# 2-1. 만약 이동한 방향에 플레이어가 없다면
#           해당 칸에 총이 있는지 확인한다.
#           총이 있다면, 해당 플레이어는 총을 획득한다.
#               플레이어가 이미 총을 가지고 있는 경우
#               놓여있는 총등과 플레이어가 가지고 있는 총 가운데 공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둔다.

# 2-2-1. 만약 이동한 방향에 플레이어가 있다면
#           두 플레이어는 싸운다.
#           1) 두 플레이어의 초기 능력치 + 가지고 있는 총의 공격력 합을 비교
#           2) 플레이어의 초기 능력치가 높은 플레이어
#           -> 우선순위대로 이긴다.
#           이긴 플레이어는) 각 플레이어의 초기 능력치와, 가지고 있는 총의 공격력의 합의 차이 만큼 포인트를 가진다.
# 2-2-2.    진 플레이어는) 본인이 가지고 있는 총을 해당 격자에 내려 놓고, 원래 방향으로 이동한다.
#               만약 이동하려는 칸에 다른 플레이어나, 격자 범위 밖일 경우
#               오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동한다.
#                   만약 해당 칸에 총이 있다면,
#                   해당 플레이어는 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓는다.
# 2-2-3.    이긴 플레이어는) 승리한 칸에 떨어져 있는 총들과, 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓는다.
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
ARR = []
for _ in range(N):
    input_list = list(map(int, input().split()))
    output_list = []
    for val in input_list:
        if val == 0:
            output_list.append([])
        else:
            output_list.append([val])
    ARR.append(output_list)

player_loc = []
player_dist = []
player_init_power = []
player_gun_list = [0] * M
player_point_list = [0] * M
for _ in range(M):
    x, y, d, s = map(int, input().split())
    x, y = x - 1, y - 1
    player_loc.append((x, y))
    player_dist.append(d)
    player_init_power.append(s)
dist_info = {
    0: (-1, 0),  # 상
    1: (0, 1),  # 우
    2: (1, 0),  # 하
    3: (0, -1)  # 좌
}


def in_box(i, j):
    return 0 <= i < N and 0 <= j < N


def mv_player(idx):
    ci, cj = player_loc[idx]
    dist = player_dist[idx]

    di, dj = dist_info[dist]
    ni, nj = ci + di, cj + dj
    if not in_box(ni, nj):
        dist = (dist + 2) % 4
        di, dj = dist_info[dist]
        ni, nj = ci + di, cj + dj
    return ni, nj, dist


def find_next_player(i, j, my_idx):
    next_player = None
    for npi in range(M):
        if my_idx == npi:
            continue
        nci, ncj = player_loc[npi]
        if (i, j) == (nci, ncj):
            next_player = npi

    return next_player


def get_gun(arr, i, j, player_gun):
    # 2-1. 만약 이동한 방향에 플레이어가 없다면
    #           해당 칸에 총이 있는지 확인한다.
    #           총이 있다면, 해당 플레이어는 총을 획득한다.
    #               플레이어가 이미 총을 가지고 있는 경우
    #               놓여있는 총등과 플레이어가 가지고 있는 총 가운데 공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둔다.
    if not arr[i][j]:
        return arr, player_gun
    if player_gun == 0:
        new_gun = arr[i][j][-1]
        arr[i][j] = arr[i][j][:-1]
        return arr, new_gun
    else:
        arr[i][j].append(player_gun)
        arr[i][j] = sorted(arr[i][j])
        new_gun = arr[i][j][-1]
        arr[i][j] = arr[i][j][:-1]
        return arr, new_gun


def pull_gun(arr, i, j, gun):
    if gun == 0:
        return arr
    arr[i][j].append(gun)
    arr[i][j] = sorted(arr[i][j])
    return arr


def fight(first_player_index, second_player_index):
    # 2-2-1. 만약 이동한 방향에 플레이어가 있다면
    #           두 플레이어는 싸운다.
    #           1) 두 플레이어의 초기 능력치 + 가지고 있는 총의 공격력 합을 비교
    #           2) 플레이어의 초기 능력치가 높은 플레이어
    #           -> 우선순위대로 이긴다.
    #           이긴 플레이어는) 각 플레이어의 초기 능력치와, 가지고 있는 총의 공격력의 합의 차이 만큼 포인트를 가진다.
    # 2-2-2.    진 플레이어는) 본인이 가지고 있는 총을 해당 격자에 내려 놓고, 원래 방향으로 이동한다.
    #               만약 이동하려는 칸에 다른 플레이어나, 격자 범위 밖일 경우
    #               오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동한다.
    #                   만약 해당 칸에 총이 있다면,
    #                   해당 플레이어는 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓는다.
    # 2-2-3.    이긴 플레이어는) 승리한 칸에 떨어져 있는 총들과, 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓는다.
    first_player_init_power, second_player_init_power = player_init_power[first_player_index], player_init_power[
        second_player_index]
    first_player_gun, second_player_gun = player_gun_list[first_player_index], player_gun_list[second_player_index]

    winner, looser = None, None
    if (first_player_init_power + first_player_gun, first_player_init_power) > (
            second_player_init_power + second_player_gun, second_player_init_power):
        winner, looser = first_player_index, second_player_index
    else:
        winner, looser = second_player_index, first_player_index

    return winner, looser


def cal_point(win, loos):
    winner_init_power, looser_init_power = player_init_power[win], player_init_power[loos]
    winner_gun, looser_gun = player_gun_list[win], player_gun_list[loos]
    return winner_init_power + winner_gun - (looser_init_power + looser_gun)


def mv_looser(player_index):
    # 2-2-2.    진 플레이어는) 본인이 가지고 있는 총을 해당 격자에 내려 놓고, 원래 방향으로 이동한다.
    #               만약 이동하려는 칸에 다른 플레이어나, 격자 범위 밖일 경우
    #               오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동한다.
    #                   만약 해당 칸에 총이 있다면,
    #                   해당 플레이어는 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓는다.
    ci, cj = player_loc[player_index]
    dist = player_dist[player_index]
    di, dj = dist_info[dist]
    ni, nj = ci + di, cj + dj
    while True:
        if not in_box(ni, nj) or find_next_player(ni, nj, player_index):
            dist = (dist + 1) % 4
            di, dj = dist_info[dist]
            ni, nj = ci + di, cj + dj
            continue
        break
    return ni, nj, dist


for _ in range(K):

    for player_index in range(M):
        # 1-1. 첫 번째 플레이어 부터 순차적으로
        #       본인이 향하고 있는 방향대로 한 칸 이동한다.
        #       해당 방향으로 나갈 때, 만약 격자를 벗어나는 경우 정반대 방향으로 방향을 바꾸어 1 만큼 이동한다.
        ni, nj, ndist = mv_player(player_index)
        player_loc[player_index] = ni, nj
        player_dist[player_index] = ndist

        # 2-1. 만약 이동한 방향에 플레이어가 없다면
        #           해당 칸에 총이 있는지 확인한다.
        #           총이 있다면, 해당 플레이어는 총을 획득한다.
        #               플레이어가 이미 총을 가지고 있는 경우
        #               놓여있는 총등과 플레이어가 가지고 있는 총 가운데 공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둔다.
        next_player_index = find_next_player(ni, nj, player_index)
        if next_player_index is None:
            player_gun = player_gun_list[player_index]
            ARR, new_player_gun = get_gun(ARR, ni, nj, player_gun)
            player_gun_list[player_index] = new_player_gun
        # 2-2-1. 만약 이동한 방향에 플레이어가 있다면
        #           두 플레이어는 싸운다.
        #           1) 두 플레이어의 초기 능력치 + 가지고 있는 총의 공격력 합을 비교
        #           2) 플레이어의 초기 능력치가 높은 플레이어
        #           -> 우선순위대로 이긴다.
        #           이긴 플레이어는) 각 플레이어의 초기 능력치와, 가지고 있는 총의 공격력의 합의 차이 만큼 포인트를 가진다.
        # 2-2-2.    진 플레이어는) 본인이 가지고 있는 총을 해당 격자에 내려 놓고, 원래 방향으로 이동한다.
        #               만약 이동하려는 칸에 다른 플레이어나, 격자 범위 밖일 경우
        #               오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동한다.
        #                   만약 해당 칸에 총이 있다면,
        #                   해당 플레이어는 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓는다.
        # 2-2-3.    이긴 플레이어는) 승리한 칸에 떨어져 있는 총들과, 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓는다.
        else:
            winner_index, looser_index = fight(player_index, next_player_index)
            # 이긴 플레이어 포인트 얻기
            point = cal_point(winner_index, looser_index)
            player_point_list[winner_index] += point

            # 진 플레이어 총 놓기
            looser_gun = player_gun_list[looser_index]
            player_gun_list[looser_index] = 0
            ARR = pull_gun(ARR, ni, nj, looser_gun)
            # 진 플레이어 이동하기
            looser_i, looser_j, looser_dist = mv_looser(looser_index)
            player_loc[looser_index] = looser_i, looser_j
            player_dist[looser_index] = looser_dist
            # 해당 위치에 총이 있다면 위와 동일하게 총을 얻는다.
            ARR, new_looser_gun = get_gun(ARR, looser_i, looser_j, 0)
            player_gun_list[looser_index] = new_looser_gun

            # 이긴 플레이어 지금 칸에서 총 얻기
            winner_gun = player_gun_list[winner_index]
            ARR, new_winner_gun = get_gun(ARR, ni, nj, winner_gun)
            player_gun_list[winner_index] = new_winner_gun

print(*player_point_list)