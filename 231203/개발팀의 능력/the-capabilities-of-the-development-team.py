import sys
arr = list(map(int, input().split()))
min_cnt = sys.maxsize

check = 0
sample = []
for i in range(5):
    a = arr[i]
    s = arr[:i] + arr[i+1:]
    for j in range(4):
        for k in range(j+1,4):
            b = s[j] + s[k]
            c = sum(s[:j] + s[j+1:k] + s[k+1:])
            if a == b or a == c or b == c:
                continue
            k = max(a, b, c) - min(a, b, c)
            if k < min_cnt:
                check = 1
                min_cnt = k
if check:
    print(min_cnt)
else:
    print(-1)