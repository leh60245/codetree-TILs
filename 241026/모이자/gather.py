import sys

INT_MIN = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    min_len = 0
    for j in range(len(arr)):
        min_len += abs(i-j) * arr[j]
    INT_MIN = min(INT_MIN, min_len)

print(INT_MIN)