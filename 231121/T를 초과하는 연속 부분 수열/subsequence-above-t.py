n, t = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
cnt = 0
for idx, i in enumerate(arr):
    if i > t:
        cnt += 1
    else:
        if answer < cnt:
            answer = cnt
        cnt = 0

print(answer)