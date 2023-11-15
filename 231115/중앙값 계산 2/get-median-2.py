import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

sample_arr = [arr[0]]
print(arr[0], end=' ')
for i in range(1, n):
    for j in range(len(sample_arr)):
        if sample_arr[j] > arr[i]:
            sample_arr = sample_arr[:j] + [arr[i]] + sample_arr[j:]
            break
        if j == len(sample_arr) - 1:
            sample_arr.append(arr[i])
    if i % 2 == 0:
        print(sample_arr[len(sample_arr)//2], end=' ')