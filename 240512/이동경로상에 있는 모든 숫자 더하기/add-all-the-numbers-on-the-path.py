n, t = map(int, input().split())
cmd = input()
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arrow_cmd = {"L":-1, "R":1, "F":0}
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
point = (n//2, n//2)    # y, x
arrow = 0
answer = 0 + arr[point[0]][point[1]]
for i in range(t):
    now_cmd = cmd[i]
    arrow = (arrow + arrow_cmd[now_cmd]) % 4
    if now_cmd == "F":
        if point[0]+dy[arrow] < 0 or point[0]+dy[arrow] >= n or point[1]+dx[arrow] < 0 or point[1]+dx[arrow] >= n:
            continue
        point = (point[0]+dy[arrow], point[1]+dx[arrow])
        answer += arr[point[0]][point[1]]
print(answer)