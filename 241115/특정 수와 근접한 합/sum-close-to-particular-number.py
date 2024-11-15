n, s = map(int, input().split())
arr = list(map(int, input().split()))

all_sum = sum(arr)
min_diff = float('inf') 


for i in range(n - 1):
    for j in range(i + 1, n):

        current_sum = all_sum - arr[i] - arr[j]

        diff = abs(current_sum - s)
 
        if diff < min_diff:
            min_diff = diff

print(min_diff)
