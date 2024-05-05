n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(m):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
    count = 0 
    for j in range(4):
        rr, cc = r-1+dx[j], c-1+dy[j]
        if 0 > rr or rr >= n or 0 > cc or cc >= n:
            continue
        if arr[r-1+dx[j]][c-1+dy[j]] == 1:
            count += 1
    if count == 3:
        print(1)
    else:
        print(0)