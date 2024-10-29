n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
for i in range(n-k+1):
    tmp = sum(arr[i:i+k])
    if tmp > answer:
        answer = tmp

print(answer)