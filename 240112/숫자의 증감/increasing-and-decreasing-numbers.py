c, n = map(str, input().split())
n = int(n)
if c == 'A':
    for i in range(1, n+1):
        print(i, end=" ")
elif c == "D":
    for j in range(n,0,-1):
        print(j, end=" ")