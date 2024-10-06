import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_box(x, y):
    return x < n and x >= 0 and y < n and y >= 0


def mv(x, y):
    chk = -1
    sv_big = arr[x][y]
    for i in range(4):
        mv_x, mv_y = x + dx[i], y + dy[i]
        if in_box(mv_x, mv_y) and arr[mv_x][mv_y] > sv_big:
            chk = i
            break
    return chk


ans = [arr[r-1][c-1]]
while True:
    i = mv(r - 1, c - 1)
    if i == -1:
        break

    r, c = r + dx[i], c + dy[i]
    ans.append(arr[r-1][c-1])

print(*ans)