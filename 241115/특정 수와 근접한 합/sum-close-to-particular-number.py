n, s = map(int, input().split())
arr = list(map(int, input().split()))
all_arr = sum(arr)
ans = abs(all_arr - s)
arr.sort()
for i in range(n - 1):
    for j in range(i + 1, n):
        tmp = abs(s - abs(all_arr - arr[i] - arr[j]))
        if tmp < ans:
            ans = tmp

print(ans)
