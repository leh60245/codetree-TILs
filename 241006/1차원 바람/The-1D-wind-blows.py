import sys

input = sys.stdin.readline
n, m, q = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
r, d = map(str, input().split())
r = int(r)
direction = ["L", "R"]  # L은 바람이 왼쪽에서 불어온다는 것


def sol(idx, direct, end):
    if idx < 0 or idx >= n:
        return
    if idx in end:
        return
    if direct == "L":
        tmp = arr[idx][-1]
        for i in range(m - 2, -1, -1):
            arr[idx][i + 1] = arr[idx][i]
        arr[idx][0] = tmp
    else:
        tmp = arr[idx][0]
        for i in range(1, m):
            arr[idx][i - 1] = arr[idx][i]
        arr[idx][-1] = tmp

    if idx > 0 and chk(idx, "up"):
        if direct == "L":
            sol(idx - 1, "R", end + [idx])
        else:
            sol(idx - 1, "L", end + [idx])
    if idx < n-1 and chk(idx, "down"):
        if direct == "L":
            sol(idx + 1, "R", end + [idx])
        else:
            sol(idx + 1, "L", end + [idx])

    return


def chk(idx, op):
    if op == "up":
        for i in range(m):
            if arr[idx][i] == arr[idx - 1][i]:
                return True
    else:
        for i in range(m):
            if arr[idx][i] == arr[idx + 1][i]:
                return True
    return False


for _ in range(q):
    sol(r - 1, d, [])
for i in range(n):
    print(*arr[i])