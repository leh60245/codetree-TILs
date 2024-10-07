import sys
from collections import deque

input = sys.stdin.readline
L, N, Q = map(int, input().split())
# 0: 빈칸, 1: 함정, 2: 벽
arr = list()
for i in range(L):
    input_list = list(map(int, input().split()))
    arr.append(input_list)

# (r, c, h, w, k):
# 처음 위치 좌측 상단 (r, c)
# 세로 h, 가로 w
# 체력 k
# 저장할 때는 0부터 시작하는 인덱스로
org_knights = list()
knights = list()
for _ in range(N):
    r, c, h, w, k = map(int, input().split())
    r, c = r - 1, c - 1
    org_knights.append((r, c, h, w, k))
    knights.append((r, c, h, w, k))

# (i, d): i번 기사에게 방향 d로 한 칸 이동.
# 1<=i<=N. 단, 사라진 기사 번호일 수 있다.
# d = 0, 1, 2, 3 : 위, 오, 아, 왼
# 저장할 때는 0부터 시작하는 인덱스로
commands = list()
for _ in range(Q):
    i, d = map(int, input().split())
    i = i - 1
    commands.append((i, d))
directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
#
# print(arr)
# print(knights)
# print(commands)

# [1] 기사 이동
# 1. 만약 이동하려는 위치에 다른 기사가 있다면,
#   -> 그 기사도 함께 한 칸 밀려난다.
#   -> 그 옆에 또 기사가 있다면 연쇄적으로 밀린다.
# 1.1 하지만 기사가 이동하려는 방향 끝에 벽이 있다면
#   -> 모든 기사는 이동할 수 없다.
# 2. 없는 기사는 아무 반응 x
# [2] 대결
# 1. 밀려난 기사'들'은 피해를 입는다.
#   -> 이동한 곳에 (이동한 후에) w * h 직사각형 내 놓여 있는 '함정 수'만큼 피해를 입는다.
#   -> 각 기사마다 피해를 받은 만큼 체력이 깍이며, 현재 체력 이상의 대미지를 받는다면 체스판에서 사라진다.
# 2. 단, 명령을 받은 기사는 '피해를 입지 않는다.'
# 주의) 기사들은 모두 '밀린 이후에' 대미지를 입는다.
# 3. 밀렸더라도 밀쳐진 위치에 함정이 전혀 없다면 기사는 피해를 전혀 입지 않는다.

def in_box(i, j):
    return 0 <= i < L and 0 <= j < L


# knight의 size 만큼의 index list를 제공해 주면서, 그 안에 함정 수도 제공
def size_knight(idx):
    index_list = list()
    r, c, h, w, _ = knights[idx]
    num_traps = 0
    for i in range(h):
        for j in range(w):
            nr, nc = r + i, c + j
            index_list.append((nr, nc))
            if arr[nr][nc]:
                num_traps += 1
    return index_list, num_traps


# 밀어도 되는 지 확인 후 밀게 되는 knight의 인덱스들 반환
# 주의) 들어온 인덱스의 값은 그냥 0부터 시작한다고 합시다.
def bfs(index_knight, direction_knight):
    # [1] 생성
    q = deque()
    v = [
        [0] * L for _ in range(L)
    ]

    # [2] 초기 설정
    index_list, _ = size_knight(index_knight)
    for i, j in index_list:
        q.append((i, j))
        v[i][j] = 1

    # 한쪽 방향에 있는 knights를 찾아야 함.
    # 체력이 없는 knight는 건너 뜀
    # 만약 빈 칸, 함정이라면 상관 x.
    # 벽이라면 while문을 끝내고 밀 수 없음을 알려야 함.
    mv_knights_list = []
    while q:
        ci, cj = q.popleft()
        ni, nj = ci + directions[direction_knight][0], cj + directions[direction_knight][1]
        if not in_box(ni, nj) or arr[ni][nj] == 2:
            return []
        if not v[ni][nj]:
            # 다음 위치가 knight인지 확인
            for next_knight_index, knight_info in enumerate(knights):
                # 자신은 제거
                if next_knight_index == index_knight:
                    continue
                nr, nc, nh, nw, nk = knight_info
                if nk == 0:  # 죽은 기사는 제거
                    continue
                next_knight_index_list, _ = size_knight(next_knight_index)
                # knight가 맞다면,
                if (ni, nj) in next_knight_index_list:
                    # print(next_knight_index)
                    for nki, nkj in next_knight_index_list:
                        v[nki][nkj] = 1
                        q.append((nki, nkj))
                        if next_knight_index not in mv_knights_list:
                            mv_knights_list.append(next_knight_index)
    # for i in range(L):
    #     print(*v[i])
    # 턴이 끝나고 밀리는 knights들의 index 반환
    return mv_knights_list


# 밀린 이후 밀려진 knights의 list를 받아 knights를 밈
# knights의 인덱스를 받아 좌표 수정
def mv_knights(lst, direction_knight):
    global knights
    for idx in lst:
        r, c, h, w, k = knights[idx]
        r, c = r + directions[direction_knight][0], c + directions[direction_knight][1]
        knights[idx] = (r, c, h, w, k)


# 밀린 이후 밀려진 knights의 index list를 받아 데미지를 줌
def chk_dmg(lst):
    global knights
    for idx in lst:
        r, c, h, w, k = knights[idx]
        _, dmg = size_knight(idx)
        k = max(k - dmg, 0)
        knights[idx] = (r, c, h, w, k)

start = 0
for command in commands:
    cmd_index_knight, cmd_direction_knight = command
    # print("start: ", start)
    # print("knight index:", cmd_index_knight)
    # 체력이 없는 기사에 대한 명령은 무시
    if knights[cmd_index_knight][-1] <= 0:
        continue
    result = bfs(cmd_index_knight, cmd_direction_knight)
    # print(result)
    mv_knights(result, cmd_direction_knight)
    chk_dmg(result)

    # print(knights)

    start += 1

ans = 0
for i in range(N):
    _, _, _, _, nk = knights[i]
    if nk <= 0:
        continue
    _, _, _, _, ok = org_knights[i]
    ans += ok - nk

print(ans)