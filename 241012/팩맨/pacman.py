# 4x4 격자, m개 몬스터, 1개 픽맨
# 몬스터는 상하좌우, 대각선 방향 중 하나

# <턴 설명. 한 턴은 다음과 같이 진행된다.>
# [1] 몬스터 복제 시도
# 몬스터는 '현재 위치'에서 '자신과 같은 방향'을 가진 못느터를 복제하려 한다
# 이 복제된 알 몬스터는 움직이지 못한다.
# ******* 복제된 시점을 기준으로 각 몬스터와 동일한 방향을 기자며, 이후 이 알이 부화할 시 해당 방향을 지지며 깨어난다.****
#       -> 복제되는 시점에 알의 위치와 함께 방향을 저장해야 한다.
#       -> 알 끼리(몬스터끼리) 구분하는 것은 방향이라, 우선 이차원 격자에 방향을 저장하자
#       -> 알이 생긴 위치에서 알은 변하지 않으니, 이차원 격자에 방향을 저장해서 두자.
#       -> 알끼리 한 칸에 겹칠 경우.

# [2] 몬스터 이동
# 현재 자신이 가진 방향대로 한 칸 이동한다.
# if 움직이려는 칸에 몬스터의 시체가 있거나 OR 픽맨이 잇는 경우 OR 격자를 벗어나는 경우
#       반 시계 방향으로 45도 회전한 뒤 해당 방향으로 갈 수 있는지 판단
#       갈 수 없다면, 가능할 때까지 반시계 방향으로 45도씩 회전하며 확인
#       IF 모든 방향이 움직일 수 없다면,
#           몬스터는 움직이지 않는다.


# [3] 픽맨 이동
# 총 3칸을 이동한다. ******각 이동마다 상하좌우 선택지를 가진다.****
# 따라서 64개의 이동 방법이 존재하는데, 이 중 몬스터를 가장 많이 먹을 수 잇는 방향으로 움직인다. -> 완전 탐색
# 많이 먹을 수 있는 방법이 여러개라면, 상-좌-하-우 우선순위를 가진다. 상상상-상상좌-상상하-상상우-상좌상-상좌좌-...
# 이동하는 과정에 격자 밖을 나가는 경우는 고려하지 않는다.
# 이동하는 과정에서 이동하는 칸에 있는 몬스터는 모두 먹고, 그 자리에 몬스터 시체를 남긴다. -> 벽(몬스터에게만 해당)
# 단, 픽맨은 알은 먹지 않으며, 움직이기 전에 함께 있었던 몬스터도 먹지 않는다.
#   **********즉 이동하는 과정에 있는 몬스터만 먹는다. **********

# [4] 몬스터 시체 소멸
# 시체는 2턴동안 유지 -> dead_arr에 2로 표시 후 모두 1 씩 감소 max( ? , 0),
# 시체 위에 새로운 시체가 생길 순 없다.

# [5] 몬스터 복제 완성
# 알 형태 몬스터가 부화한다. 처음 복제가 된 몬스터의 방향을 지닌 채 깨어난다.

# [] 입력
# 1. 몬스터 마리 m, 턴 수 t
# 2. 픽맨의 격자 초기 위치 r, c
# 3. 이후 m개 줄에 r, c, d(방향). 방향은 0~7까지 위에서 시계방향 45도
# t 턴이 지나고 격자에 살아남은 몬스터의 수는 몇 마리인가

import sys

input = sys.stdin.readline

# [] 입력
# 1. 몬스터 마리 m, 턴 수 t
# 2. 픽맨의 격자 초기 위치 r, c
# 3. 이후 m개 줄에 r, c, d(방향). 방향은 0~7까지 위에서 시계방향 45도
# t 턴이 지나고 격자에 살아남은 몬스터의 수는 몇 마리인가
ARRLEN = 4
M, T = map(int, input().split())
R, C = map(int, input().split())
R, C = R - 1, C - 1

### 고스트 변경마다 갱신해야 하는 부분 - [2] 위치와 방향 변경. [3] 삭제, [5] 새롭게 생성
gost_arr = [[0] * ARRLEN for _ in range(ARRLEN)]  # 격자위 고스트 마리 수
gost_info = list()  # r, c, d 저장
for _ in range(M):
    r, c, d = map(int, input().split())
    r, c, d = r - 1, c - 1, d - 1
    gost_arr[r][c] += 1
    gost_info.append((r, c, d))

### 시체 변경 - [3] 생성 [4] 삭감
dead_arr = [[0] * ARRLEN for _ in range(ARRLEN)]  # 시체 표기

dist_info = {
    0: (-1, 0),
    1: (-1, -1),
    2: (0, -1),
    3: (1, -1),
    4: (1, 0),
    5: (1, 1),
    6: (0, 1),
    7: (-1, 1)
}


############################################################

def in_box(i, j):
    return 0 <= i < ARRLEN and 0 <= j < ARRLEN


def mv_gost(info):
    # [2] 몬스터 이동
    # 현재 자신이 가진 방향대로 한 칸 이동한다.
    # if 움직이려는 칸에 몬스터의 시체가 있거나 OR 픽맨이 잇는 경우 OR 격자를 벗어나는 경우
    #       반시계 방향으로 45도 회전한 뒤 해당 방향으로 갈 수 있는지 판단
    #       갈 수 없다면, 가능할 때까지 반시계 방향으로 45도씩 회전하며 확인
    #       IF 모든 방향이 움직일 수 없다면,
    #           몬스터는 움직이지 않는다.
    new_arr = [[0] * ARRLEN for _ in range(ARRLEN)]
    new_info = list()
    for ci, cj, cdist in info:
        cdist -= 1
        can_move = False
        for _ in range(8):
            cdist = (cdist + 1) % 8
            di, dj = dist_info[cdist]
            ni, nj = ci + di, cj + dj
            if not in_box(ni, nj) or (ni, nj) == (R, C) or dead_arr[ni][nj]:
                continue
            else:
                new_arr[ni][nj] += 1
                new_info.append((ni, nj, cdist))
                can_move = True
                break
        if not can_move:
            cdist += 1
            new_arr[ci][cj] += 1
            new_info.append((ci, cj, cdist))
    return new_arr, new_info


def mv_pickman(ci, cj, gost_arr, gost_info, dead_arr):
    # [3] 픽맨 이동
    # 총 3칸을 이동한다. ******각 이동마다 상좌하우 선택지를 가진다.****
    # 따라서 64개의 이동 방법이 존재하는데, 이 중 몬스터를 가장 많이 먹을 수 잇는 방향으로 움직인다. -> 완전 탐색
    # 많이 먹을 수 있는 방법이 여러개라면, 상-좌-하-우 우선순위를 가진다. 상상상-상상좌-상상하-상상우-상좌상-상좌좌-...
    # 이동하는 과정에 격자 밖을 나가는 경우는 고려하지 않는다.
    # 이동하는 과정에서 이동하는 칸에 있는 몬스터는 모두 먹고, 그 자리에 몬스터 시체를 남긴다. -> 벽(몬스터에게만 해당)
    # 단, 픽맨은 알은 먹지 않으며, 움직이기 전에 함께 있었던 몬스터도 먹지 않는다.
    #   **********즉 이동하는 과정에 있는 몬스터만 먹는다. **********
    max_eat = -1  # 정말 만약에라도 먹을 고스트가 없다면, 움직이긴 해야 하니까...
    path = list()
    for fdi, fdj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        fni, fnj = ci + fdi, cj + fdj
        if not in_box(fni, fnj) or (fni, fnj) == (ci, cj):
            continue
        for sdi, sdj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            sni, snj = ci + fdi + sdi, cj + fdj + sdj
            if not in_box(sni, snj) or (sni, snj) == (fni, fnj) or (sni, snj) == (ci, cj):
                continue
            for tdi, tdj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                tni, tnj = ci + fdi + sdi + tdi, cj + fdj + sdj + tdj
                if not in_box(tni, tnj) or (tni, tnj) == (sni, snj) or (tni, tnj) == (fni, fnj) or (tni, tnj) == (
                ci, cj):
                    continue
                eat = gost_arr[fni][fnj] + gost_arr[sni][snj] + gost_arr[tni][tnj]
                if max_eat < eat:
                    max_eat = eat
                    path = [(fni, fnj), (sni, snj), (tni, tnj)]

    # 정말 만약에라도 먹을 고스트가 없다면, 위위위로 올라가야한다.

    # 경로상의 몬스터 죽이기
    new_gost_info = []
    for gi, gj, gd in gost_info:
        if (gi, gj) in path:
            gost_arr[gi][gj] -= 1
            dead_arr[gi][gj] = 3
        else:
            new_gost_info.append((gi, gj, gd))

    after_R, after_C = path[-1]
    return after_R, after_C, gost_arr, new_gost_info, dead_arr


for _ in range(T):
    # [1] 몬스터 복제 시도
    # 몬스터는 '현재 위치'에서 '자신과 같은 방향'을 가진 못느터를 복제하려 한다
    # 이 복제된 알 몬스터는 움직이지 못한다.
    # ******* 복제된 시점을 기준으로 각 몬스터와 동일한 방향을 기자며, 이후 이 알이 부화할 시 해당 방향을 지니며 깨어난다.****
    #       -> 복제되는 시점에 알의 위치와 함께 방향을 저장해야 한다.
    eggs_info = gost_info[:]

    # [2] 몬스터 이동
    gost_arr, gost_info = mv_gost(gost_info)

    # [3] 픽맨 이동
    R, C, gost_arr, gost_info, dead_arr = mv_pickman(R, C, gost_arr, gost_info, dead_arr)

    # [4] 몬스터 시체 소멸
    # 시체는 2턴동안 유지 -> dead_arr에 2로 표시 후 모두 1 씩 감소 max( ? , 0),
    # 시체 위에 새로운 시체가 생길 순 없다.
    for i in range(ARRLEN):
        for j in range(ARRLEN):
            dead_arr[i][j] = max(dead_arr[i][j] - 1, 0)

    # [5] 몬스터 복제 완성
    # 알 형태 몬스터가 부화한다. 처음 복제가 된 몬스터의 방향을 지닌 채 깨어난다.
    for gi, gj, gd in eggs_info:
        gost_info.append((gi, gj, gd))
        gost_arr[gi][gj] += 1

answer = 0
for i in gost_arr:
    answer += sum(i)
print(answer)