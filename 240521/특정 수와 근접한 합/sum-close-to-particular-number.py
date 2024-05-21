n, s = map(int, input().split())
arr = list(map(int, input().split()))
save = sum(arr[2:])
for i in range(n):
    for j in range(i+1, n):
        k = sum(arr[:i] + arr[i+1:j] + arr[j+1:])
        if abs(s-k) < abs(s-save):
            save = k
print(abs(save-s))