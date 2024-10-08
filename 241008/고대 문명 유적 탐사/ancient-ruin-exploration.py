import sys
from collections import deque

input = sys.stdin.readline
# K: 탐사 반복 횟수, M: 벽면에 적힌 유물 조각 개수
# 1 <= K <= 10, 10 <= M <= 300
# 1 <= 조각 번호 <= 7
K, M = map(int, input().split())
arr = []
for _ in range(5):  # 5개 고정
    input_list = list(map(int, input().split()))
    arr.append(input_list)
scrap_numbers = list(map(int, input().split()))  # 길이 M


# [1] 탐사 진행
# 3*3 격자 선택 -> 시계 방향 90, 180, 270도 중 '하나의' 각도만큼 회전시킬 수 있다.
# 회전 중심 좌표를 제공한다.
# 회전 목표:
# 가능한 회전 중
#   1) 유물 1차 획득 가치 최대화 -> 만약 방법이 여러가지 라면 2번으로
#   2) 회전한 각도가 가장 작은 방법 선택: 우선 순위 90도 > 180도 > 270도
#   3) 회전 중심 좌표의 열이 작은 구간, 마지막으로 행이 가장 작은 구간 선택

# [2] 유물 획득
# [2-1] 유물 1차 획득
# 상하좌우로 인접한 같은 종류의 유물 조각은 '서로 연결'되어 있다.
#   -> '조각들'이 '3개 이상' 연결된 경우, -> 조각이 모여 '유물'이 되고 '사라진다'.
#   -> 유물의 가치는 모인 조각의 """개수""" 와 같다.
# 유물 생성
# 벽면에는 1부터 7 사이 숫자 M개가 있다. 이들은 유적에서 '조각이 사라졌을 때' 새로 생겨나는 조각에 대한 정보다.
# 조각이 사라진 위치에는 유적 벽면에 적힌 순서대로 새로운 조각이 생긴다.
#   1) 열 번호가 "작은" 순
#   2) 열 번호가 같다면, 행 번호가 "큰" 순
# 벽면의 숫자가 부족한 경우는 없다.
# [2-2] 유물 연쇄 획득
# 더 이상 조각이 3개 이상 연결되지 않아 유물이 될 수 없을 때까지 반복된다.
# [3] 탐사 반복
# 1턴 = [1] 탐사 진행 ~ [2-2] 유물 연쇄 획득
# 만약 K번의 턴을 진행하지 못했지만, 탐사 진행 과정에서 어떠한 방법을 사용하더라도 유물을 획득할 수 없다면,
# 그 즉시 탐사는 종료된다. 이 경우, 얻을 수 있는 유물이 존재하지 않음으로, 종료되는 턴에 아무 값도 출력하지 않는다.


# 회전의 좌측 상단 좌표를 받는다.
def rotate_90(sx, sy, lenght, cnt):
    new_arr = [i[:] for i in arr]

    for x in range(sx, sx + lenght):
        for y in range(sy, sy + lenght):
            # 0, 0 으로 옮겨주기
            ox, oy = x - sx, y - sy
            # 90도 회전 후의 좌표
            for _ in range(cnt):
                ox, oy = oy, lenght - ox - 1
            # 다시 sy, sx를 더해줌
            new_arr[sx + ox][sy + oy] = arr[x][y]

    return new_arr


def in_box(i, j):
    return 0 <= i < 5 and 0 <= j < 5


def bfs(start_i, start_j, look_arr):
    q = deque()
    global visited
    visited_index = []
    start_type = look_arr[start_i][start_j]  # 유물 번호

    q.append((start_i, start_j))
    visited[start_i][start_j] = 1
    visited_index.append((start_i, start_j))

    cnt = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if in_box(ni, nj) and not visited[ni][nj] and look_arr[ni][nj] == start_type:
                visited[ni][nj] = 1
                q.append((ni, nj))
                visited_index.append((ni, nj))
                cnt += 1

    return cnt, visited_index



for _ in range(K):  # 탐사 반복 횟수. 중간에 나올 수 있다.
    ans = 0
    # print("start")
    # 유물 1차 획득
    first_result = (0, 4, 5, 5, [], [])  # (value, rotate, j, i, before_zero_blocks)
    for rotate in [3, 2, 1]:
        for j in range(2, -1, -1):
            for i in range(2, -1, -1):
                rotate_arr = rotate_90(i, j, 3, rotate)
                # for arrarr in rotate_arr:
                #     print(arrarr[:])
                visited = [[0] * 5 for _ in range(5)]
                value = 0
                before_zero_blocks = []
                for start_i in range(5):
                    for start_j in range(5):
                        if visited[start_i][start_j]:
                            continue
                        cnt, visited_index = bfs(start_i, start_j, rotate_arr)
                        if cnt >= 3:
                            value += cnt
                            before_zero_blocks += visited_index
                if (value < first_result[0]) or (rotate > first_result[1]) or (j > first_result[1]) or (
                        i > first_result[2]):
                    continue
                first_result = (value, rotate, j, i, before_zero_blocks, rotate_arr)
    if first_result[0] == 0:
        break
    ans += first_result[0]
    # print(first_result[0])

    arr = first_result[5]
    for i, j in first_result[4]:
        arr[i][j] = 0
    for j in range(5):
        for i in range(4, -1, -1):
            if arr[i][j] == 0:
                arr[i][j] = scrap_numbers.pop(0)
    # for i in arr:
    #     print(i[:])
    second_value = 0
    while True:
        visited = [[0] * 5 for _ in range(5)]
        value = 0
        before_zero_blocks = []
        for start_i in range(5):
            for start_j in range(5):
                if visited[start_i][start_j]:
                    continue
                cnt, visited_index = bfs(start_i, start_j, arr)
                if cnt >= 3:
                    value += cnt
                    before_zero_blocks += visited_index
        if value == 0:
            break
        second_value += value
        for i, j in before_zero_blocks:
            arr[i][j] = 0
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = scrap_numbers.pop(0)
    if second_value == 0:
        print(ans, end=" ")
        break
    ans += second_value
    print(ans, end=" ")

# for i in rotate_90(1, 1, 3, 2):
#     print(i[:])
"""
2 20
7 6 7 6 7
6 7 6 7 6
6 7 1 5 4
7 6 3 2 1
5 4 3 2 7
3 2 3 5 2 4 6 1 3 2 5 6 2 1 5 6 7 1 2 3

"""