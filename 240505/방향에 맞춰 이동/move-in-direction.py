dx = {"N":0, "E":1, "S":0, "W":-1}
dy = {"N":1, "E":0, "S":-1, "W":0}
n = int(input())
init = (0,0)
for i in range(n):
    a, b = map(str, input().split())
    b = int(b)
    init = (init[0]+dx[a]*b,init[1]+dy[a]*b)
print(*init)