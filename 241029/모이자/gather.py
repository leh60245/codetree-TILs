import sys
n = int(input())
arr = list(map(int, input().split()))

MIN = sys.maxsize
for i in range(n):
    cnt = 0
    for j in range(n):
        tmp = arr[j] * abs(i-j)
        cnt += tmp
    if cnt < MIN:
        MIN = cnt

print(MIN)