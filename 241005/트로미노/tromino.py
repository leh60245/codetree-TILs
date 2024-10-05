import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def chk1(x, y):
    return arr[x][y] + arr[x+1][y] + arr[x][y+1]

def chk2(x, y):
    return arr[x][y] + arr[x+1][y] + arr[x+1][y+1]

def chk3(x, y):
    return arr[x][y] + arr[x+1][y+1] + arr[x][y+1]

def chk4(x, y):
    return arr[x][y+1] + arr[x+1][y] + arr[x+1][y+1]

def chk5(x, y):
    return arr[x][y] + arr[x][y+1] + arr[x][y+2]

def chk6(x, y):
    return arr[x][y] + arr[x+1][y] + arr[x+2][y]

answer = 0
for i in range(n):
    for j in range(m-2):
        answer = max(answer, chk5(i, j))

for i in range(n-2):
    for j in range(m):
        answer = max(answer, chk6(i, j))

for i in range(n-1):
    for j in range(m-1):
        answer = max(answer, chk1(i, j), chk2(i, j), chk3(i, j), chk4(i, j))

print(answer)