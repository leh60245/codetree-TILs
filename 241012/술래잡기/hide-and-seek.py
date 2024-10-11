# NxN 격자. 술래는 중앙 ( N//2, N//2 )

# M명의 도망자. 좌우 유형 & 상하 유형 두 가지.
# 좌우 유형은 오른쪽을 보고 시작. 상하 유형은 아래쪽 보며 시작

# h개의 나무
# 나무 위치에 도망자가 초기 겹치는것 가능.
# 1턴 = m명 도망자 움직이고 + 술래 움직이고
# 총 K턴

# 도망자 움직이기
# 거리가 3 이하인 도망자만 움직이기. 두사람 거리는 칸의 개수
# 이번 턴에 도암치는 도망자의 규칙은 아래와 같다.
# 1) *바라보는 방향*으로 1칸 움직였을 때, 격자 밖으로 나가지 않는 경우
#   (1) 움직이려는 칸에 술래가 있다면 움직이지 않는다.
#   (2) 술래가 없다면 움직일 수 있다. 나무가 있어도 괜찮다.
# 2) *바라보는 방향*으로 1칸 움직였을 때, 격자 밖으로 나가는 경우
#   방향을 틀고 -> 바라보는 방향으로 갔을 때 술래가 없다면 한칸 이동

# 술래 움직이기
# 처음 위 방향으로 시작해 달팽이 모양으로 움직인다.
# 끝에 도달하면 걸어온 그대로 돌아가며 중앙에 돌아간다.
# 1번 턴동안 정확하게 1 칸 해당하는 방향으로 이동한다.
# 이동이 틀어지는 지점에서는 방향을 바로 바꿔준다.
# 다음으로 시야 내 도망자를 잡는다. 자신의 칸 포함하여 총 3칸이다. 항상 시야는 3칸이다.
#   이때, 나무가 있는 칸의 도망자는 잡지 못한다.
#   술래는 현재 턴이 t라면, t * (지금 턴에 잡힌 도망자 수)의 점수를 얻는다.
#   잡힌 도망자는 사라진다.

import sys

input = sys.stdin.readline
N, M, H, K = map(int, input().split())
arr = [[0] * N for _ in range(N)]

# 행, 열, 옵션, 방향
runner_info = []
dst_op = {0: {0: (0, 1),
              1: (0, -1)},
          1: {0: (1, 0),
              1: (-1, 0)}}
for _ in range(M):
    # 위치 + 옵션
    i, j, op = map(int, input().split())
    i, j, op = i - 1, j - 1, op - 1
    runner_info.append((i, j, op, 0))

tree_loc = set()
for _ in range(H):
    tree_i, tree_j = map(int, input().split())
    tree_i, tree_j = tree_i - 1, tree_j - 1
    arr[tree_i][tree_j] = 1
    tree_loc.add((tree_i, tree_j))


def in_box(i, j):
    return 0 <= i < N and 0 <= j < N


def finder_mv():
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ci = N // 2
    cj = N // 2
    dist = 1
    d_index = 0
    move_count = 0  # 2가 되면 dist + 1, move_count = 0 초기화
    answer_list = [(ci, cj)]
    look_list = [d[d_index]]
    while True:
        for _ in range(dist):
            di, dj = d[d_index]
            ni, nj = ci + di, cj + dj
            if (ni, nj) == (-1, 0):
                return answer_list, look_list[1:] + [(1, 0)]
            answer_list.append((ni, nj))
            look_list.append(d[d_index])
            ci, cj = ni, nj

        move_count += 1
        d_index = (d_index + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0


def finder_mv_reverse():
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    copy_arr = [[0] * N for _ in range(N)]
    ci, cj = 0, 0
    d_idx = 0

    answer_list = []
    look_list = []
    for _ in range(N * N):
        copy_arr[ci][cj] = 1
        di, dj = d[d_idx]
        ni, nj = ci + di, cj + dj
        if not in_box(ni, nj):
            d_idx = (d_idx + 1) % 4
            di, dj = d[d_idx]
            ni, nj = ci + di, cj + dj
            answer_list.append((ci, cj))
            look_list.append(d[d_idx])
            ci, cj = ni, nj
        else:
            if copy_arr[ni][nj]:
                d_idx = (d_idx + 1) % 4
                di, dj = d[d_idx]
                ni, nj = ci + di, cj + dj
                answer_list.append((ci, cj))
                look_list.append(d[d_idx])
                ci, cj = ni, nj
            else:
                answer_list.append((ci, cj))
                look_list.append(d[d_idx])
                ci, cj = ni, nj

    return answer_list, look_list[:-1] + [(-1, 0)]


fm, fmlook = finder_mv()
rm, rmlook = finder_mv_reverse()
finder_loc, finder_look = fm[:-1] + rm[:-1], fmlook[:-1] + rmlook[:-1]


def cal_len(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


# 도망자 움직이는 함수
def runner_mv(turn_num):
    """
[1] 도망자 움직이기
거리가 3 이하인 도망자만 움직이기. 두사람 거리는 칸의 개수
이번 턴에 도암치는 도망자의 규칙은 아래와 같다.
1) *바라보는 방향*으로 1칸 움직였을 때, 격자 밖으로 나가지 않는 경우
  (1) 움직이려는 칸에 술래가 있다면 움직이지 않는다.
  (2) 술래가 없다면 움직일 수 있다. 나무가 있어도 괜찮다.
2) *바라보는 방향*으로 1칸 움직였을 때, 격자 밖으로 나가는 경우
  방향을 틀고 -> 바라보는 방향으로 갔을 때 술래가 없다면 한칸 이동
    """
    # 술래 위치
    finder_i, finder_j = finder_loc[turn_num % len(finder_loc)]
    for runner_index in range(len(runner_info)):
        ci, cj, option, look_op = runner_info[runner_index]
        # 거리 계산
        if cal_len(ci, cj, finder_i, finder_j) > 3:
            continue

        # 나아갈 방향으로 한칸 움직였을 때
        di, dj = dst_op[option][look_op]
        ni, nj = ci + di, cj + dj
        if in_box(ni, nj):
            if (ni, nj) == (finder_i, finder_j):
                continue
            else:
                runner_info[runner_index] = ni, nj, option, look_op
        else:
            look_op = (look_op + 1) % 2
            di, dj = dst_op[option][look_op]
            ni, nj = ci + di, cj + dj
            if (ni, nj) == (finder_i, finder_j):
                runner_info[runner_index] = ci, cj, option, look_op
                continue
            else:
                runner_info[runner_index] = ni, nj, option, look_op
    return


def finder_mv(turn_num):
    """
[2] 술래 움직이기
처음 위 방향으로 시작해 달팽이 모양으로 움직인다.
끝에 도달하면 걸어온 그대로 돌아가며 중앙에 돌아간다.
1번 턴동안 정확하게 1 칸 해당하는 방향으로 이동한다.
이동이 틀어지는 지점에서는 방향을 바로 바꿔준다.
다음으로 시야 내 도망자를 잡는다. 자신의 칸 포함하여 총 3칸이다. 항상 시야는 3칸이다.
  이때, 나무가 있는 칸의 도망자는 잡지 못한다.
  술래는 현재 턴이 t라면, t * (지금 턴에 잡힌 도망자 수)의 점수를 얻는다.
  잡힌 도망자는 사라진다.
    """
    ci, cj = finder_loc[(turn_num + 1) % len(finder_loc)]
    di, dj = finder_look[(turn_num + 1) % len(finder_loc)]
    # 시야 내 도망자 잡기. runner_info에서 제외
    point = 0
    catch_runner_index = []
    for l in range(3):
        ni, nj = ci + (di * l), cj + (dj * l)
        # 박스 밖 또는 나무 위치는 넘어간다.
        if not in_box(ni, nj) or (ni, nj) in tree_loc:
            continue
        for runner_idx in range(len(runner_info)):
            ri, rj, rop, rlook = runner_info[runner_idx]
            if (ni, nj) == (ri, rj):
                point += 1
                catch_runner_index.append(runner_idx)

    point *= turn_num + 1
    new_runner_info = []
    for runner_idx in range(len(runner_info)):
        if runner_idx in catch_runner_index:
            continue
        else:
            new_runner_info.append(runner_info[runner_idx])

    return new_runner_info, point


answer = 0
for turn_number in range(K):
    # 도망자 움직이기
    runner_mv(turn_number)

    # 술래 움직이기
    runner_info, point = finder_mv(turn_number)
    answer += point

    # 도망자가 더 없다면 종료
    if not runner_info:
        break

print(answer)