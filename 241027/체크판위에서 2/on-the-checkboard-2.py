r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(map(str, input().split())))

start_i, start_j = 0, 0
color = arr[start_i][start_j]

cnt = 0
for i in range(start_i+1, r-1):
    for j in range(start_j+1, c-1):
        if arr[i][j] != color:
            for k in range(i+1, r-1):
                for l in range(j+1, c-1):
                    if arr[k][l] == color:
                        if arr[r-1][c-1] != color:
                            cnt += 1

print(cnt)