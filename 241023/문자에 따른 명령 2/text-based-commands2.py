arr = input()
d = [(0, 1), (1,0), (0,-1),(-1,0)]
cnt = 0
answer = (0,0)

for cmd in arr:
    if cmd == 'L':
        cnt = (cnt - 1) % 4
    elif cmd == 'R':
        cnt = (cnt + 1) % 4
    else:
        x, y = answer
        dx, dy = d[cnt]
        answer = x + dx, y + dy

print(*answer)