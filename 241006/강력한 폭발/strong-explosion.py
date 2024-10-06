import sys

input = sys.stdin.readline
answer = 0
n = int(input())
arr = []        # 그림
boom_index = [] # 폭탄 인덱스 리스트
CNT = 0         # 폭탄 개수
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(n):
        if row[j]:
            CNT += 1
            boom_index.append((i, j))
visited = [0] * CNT # 어떤 타입의 폭탄인지 체크

booms = {
    1: [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)],
    2: [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)],
    3: [(-1, -1), (-1, 1), (0, 0), (1, 1), (1, -1)]
}


# def boom1(x, y):
#     return [(x - 2, y), (x - 1, y), (x, y), (x + 1, y), (x + 2, y)]
#
#
# def boom2(x, y):
#     return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
#
#
# def boom3(x, y):
#     return [(x - 1, y - 1), (x - 1, y + 1), (x + 1, y + 1), (x + 1, y - 1)]

def in_box(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def sum_boom():
    tmp = [[0] * n for _ in range(n)]
    for i in range(CNT):    # 폭탄 개수
        xx, yy = boom_index[i][0], boom_index[i][1]
        for dx, dy in booms[visited[i]]:
            if in_box(xx+dx, yy+dy):
                tmp[xx+dx][yy+dy] = 1

    return sum([sum(tmp[i]) for i in range(n)])


def sol(cnt):
    global answer
    if cnt == CNT:
        answer = max(answer, sum_boom())
        return
    for i in range(1, 4):

        visited[cnt] = i
        sol(cnt + 1)
        visited[cnt] = 0

sol(0)
print(answer)