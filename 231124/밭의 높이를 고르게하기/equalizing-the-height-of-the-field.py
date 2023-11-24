import sys
n, h, t = map(int, input().split()) # h는 높이, t는 연속한 최소 횟수
arr = list(map(int, input().split()))
arr = [abs(x-h) for x in arr]

min_cnt = sys.maxsize
start, end = 0, t   # [ ..., [start, ... , ], end, ...]
while end <= n:
    min_cnt = min(sum(arr[start:end]), min_cnt)
    start += 1
    end += 1

print(min_cnt)