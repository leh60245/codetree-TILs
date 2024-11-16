import sys
n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n-t+1):
    tmp = 0
    for j in range(i, i+t):
        tmp += abs(arr[j] - h)
    ans = min(ans, tmp)

print(ans)
