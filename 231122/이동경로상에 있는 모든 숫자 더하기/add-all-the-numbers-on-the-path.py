n, t = map(int, input().split())
string = input()
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
p = 0
start_y, start_x = (n-1)//2, (n-1)//2
answer = arr[start_y][start_x]
arrow = {"R":1, "L":-1, "F":0}

for i in string:
    if arrow[i] != 0:
        p = (p + arrow[i]) % 4
    else:
        if 0 > start_y+dy[p] or start_y+dy[p] >= n or 0 > start_x+dx[p] or start_x+dx[p]  >= n:
            continue
        start_y, start_x = start_y+dy[p], start_x+dx[p] 
        answer += arr[start_y][start_x]

print(answer)