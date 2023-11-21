n = int(input())
arr = []    # [[x1, y1, x2, y2], ... ]
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

plane = [[0 for _ in range(-100, 101)] for _ in range(-100, 101)]

for idx, point in enumerate(arr):
    x1, y1, x2, y2 = point
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100
    for i in range(x1, x2):
        for j in range(y1, y2):
            plane[i][j] = 1 if idx % 2 == 0 else -1

answer = 0
for col in plane:
    answer += col.count(-1)
print(answer)