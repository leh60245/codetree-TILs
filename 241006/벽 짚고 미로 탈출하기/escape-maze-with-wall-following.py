import sys

input = sys.stdin.readline

n = int(input())
x, y = tuple(map(int, input().split()))
x, y = x - 1, y - 1
arr = []
for _ in range(n):
    st = list(map(str, input()))
    arr.append(st)
# print(arr)
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 시계 방향
idx = 0


def in_box(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def is_wall(gx, gy):
    return arr[gx][gy] == "#"


T = 0
v = []
while True:
    mx, my = x + dx[idx % 4], y + dy[idx % 4]
    # print("look", mx, my)
    if (x, y, mx, my) in v:
        # print("never end")
        T = -1
        break
    v.append((x, y, mx, my))
    if not in_box(mx, my):
        T += 1
        # print("finish")
        break
    if is_wall(mx, my):
        idx -= 1
        # print("turn left")
        continue

    wx, wy = mx + dx[(idx + 1) % 4], my + dy[(idx + 1) % 4]
    if is_wall(wx, wy):
        x, y = mx, my
        T += 1
        # print("go to front")
    else:
        x, y = wx, wy
        T += 2
        idx += 1
        # print("turn right")

print(T)