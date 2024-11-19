n, m = map(int, input().split())
arr = list()
for _ in range(n):
    arr.append(list(map(int, input().split())))

grids = {
    0: {'col': 2, 'row': 2, 'arr': [[1, 0], [1, 1]]},
    1: {'col': 2, 'row': 2, 'arr': [[0, 1], [1, 1]]},
    2: {'col': 2, 'row': 2, 'arr': [[1, 1], [0, 1]]},
    3: {'col': 2, 'row': 2, 'arr': [[1, 1], [1, 0]]},
    4: {'col': 3, 'row': 1, 'arr': [[1, 1, 1]]},
    5: {'col': 1, 'row': 3, 'arr': [[1], [1], [1]]},
}


def in_box(r, c):
    return 0 <= r < n and 0 <= c < m


ans = 0
for si in range(n):
    for sj in range(m):
        for key in grids.keys():
            col, row = grids[key]['col'], grids[key]['row']
            if not in_box(si+row-1, sj+col-1):
                continue
            tmp = 0
            for di in range(row):
                for dj in range(col):
                   tmp += arr[si+di][sj+dj] * grids[key]['arr'][di][dj]
            ans = max(ans, tmp)
print(ans)