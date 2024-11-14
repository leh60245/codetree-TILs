n, s = map(int, input().split())
arr = list(map(int, input().split()))
base = abs(sum(arr) - s)
ans = s
for i in range(n-1):
    for j in range(i+1,n):
        tmp = abs(base - arr[i] - arr[j])
        if tmp < ans:
            ans = tmp

print(ans)