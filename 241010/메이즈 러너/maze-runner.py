import sys

input = sys.stdin.readline
# N 크기 미로, M명의 참가자, K초 진행
N, M, K = map(int, input().split())
arr = []
runner_arr = [[[] for _ in range(N)] for _ in range(N)]  # 장소에 있는 러너의 index 정보
runner_info = []  # 러너의 좌표 정보
runner_move_lenght = [0] * M  # 미로에서 이동한 거리 저장
runner_is_end = [0] * M  # 러너가 출구로 나갔는지 확인

for _ in range(N):
    arr.append(list(map(int, input().split())))

for r_idx in range(M):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    arr[i][j] -= 1  # 빈 칸에 위치한 사람 수만큼 음수 값 가짐
    runner_arr[i][j].append(r_idx)
    runner_info.append((i, j))

END_I, END_J = map(int, input().split())
END_I, END_J = END_I - 1, END_J - 1
arr[END_I][END_J] = 10

# 상하좌우 순으로 배치
# 움직일 수 있는 경우 '상하'를 우선한다는 것에 기반
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def cal_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def in_box(i, j):
    return 0 <= i < N and 0 <= j < N


def mv_runner():
    for runner_index in range(M):
        # 탈출한 친구는 나가자
        if runner_is_end[runner_index]:
            continue
        ci, cj = runner_info[runner_index]  # 러너 지금 위치 가져옴
        min_lenght = cal_dist(ci, cj, END_I, END_J)
        next_i, next_j = ci, cj
        is_move = False
        for di, dj in zip(dx, dy):
            ni, nj = ci + di, cj + dj  # 러너의 다음 위치 인덱스
            # 장소 밖은 x
            if not in_box(ni, nj):
                continue
            ndist = cal_dist(ni, nj, END_I, END_J)
            # 벽이라면 넘어감 못함 1 ~ 9
            if 0 < arr[ni][nj] < 10:
                continue
            # 최단 거리 짧아지면 움직임
            if min_lenght > ndist:
                min_lenght = ndist
                next_i, next_j = ni, nj
                is_move = True
        # 위 방식으로 움직였는지 여부와, 움직였다면 어느 위치인지 정보를 알게 됨
        if is_move:
            runner_move_lenght[runner_index] += 1  # 움직인 거리 증가
            # 그리고 위치 정보 수정. 1 미로에서 +-, 2 위치에 있는 러너 인덱스 변경, 3 러너의 정보 변경 3가지
            arr[ci][cj] += 1  # 러너 사라짐
            runner_arr[ci][cj].remove(runner_index)
            # 나갔다면 끝
            if (next_i, next_j) == (END_I, END_J):
                runner_is_end[runner_index] = 1
            else:
                arr[next_i][next_j] -= 1  # 러너 추가
                runner_arr[next_i][next_j].append(runner_index)
                runner_info[runner_index] = next_i, next_j

    return


def mv_arr():
    # 박스 길이 정함
    max_square_len = N + 1  # 장소보다 1 큰 값
    for square_len in range(2, N + 1):
        for square_r in range(N - square_len+1):
            for square_c in range(N - square_len+1):

                # 하나의 정사각형 안을 check 하기
                is_runner = False
                is_exit = False
                for r in range(square_r, square_r + square_len):
                    for c in range(square_c, square_c + square_len):
                        if arr[r][c] == 10:
                            is_exit = True
                        if arr[r][c] < 0:
                            is_runner = True
                        # 만약 출구랑 최소 한 명의 러너가 들어있는 정사각형을 발견하면, 돌리고 끝낸다.
                        if is_exit and is_runner:
                            change_square(square_r, square_c, square_len)
                            return

    return


def change_square(si, sj, slen):
    global arr
    global END_I, END_J
    v = [[0] * N for _ in range(N)]

    for i in range(si, si + slen):
        for j in range(sj, sj + slen):
            # 돌려서 변경 되는 것들이 있다.
            # 1. 내구도
            if 0 < arr[i][j] < 10:
                arr[i][j] -= 1

            oi, oj = i - si, j - sj
            ni, nj = oj + si, slen - oi - 1 + sj
            v[ni][nj] = arr[i][j]

            # runner에 대한 정보 변경
            if arr[i][j] < 0:
                for runner_index in runner_arr[i][j]:  # 해당 자리에 위치한 러너들 index 가져옴
                    runner_info[runner_index] = ni, nj
                runner_arr[ni][nj] = runner_arr[i][j]
                runner_arr[i][j] = []
            # 출구에 대한 정보 변경
            if arr[i][j] == 10:
                END_I, END_J = ni, nj

    # 원본 미로 변경
    for i in range(si, si + slen):
        for j in range(sj, sj + slen):
            arr[i][j] = v[i][j]

    return


for turn in range(1, K + 1):
    # [1] 러너 이동
    mv_runner()

    # [2] 게임 끝났는지 확인
    if runner_is_end.count(1) == M:
        break

    # [3] 미로 회전
    mv_arr()

print(sum(runner_move_lenght))
print(END_I + 1, END_J + 1)