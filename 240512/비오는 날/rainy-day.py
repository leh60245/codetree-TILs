n = int(input())
answer = (2101,1,1)
save = []
for i in range(n):
    info = list(map(str, input().split(" ")))
    if info[-1] != "Rain":
        continue
    ymd = tuple(map(int, info[0].split("-")))    # (y, m, d)
    if answer[0] > ymd[0]:
        answer = ymd
        save = info
        continue
    if answer[0] == ymd[0] and answer[1] > ymd[1]:
        answer = ymd
        save = info
        continue
    if answer[0] == ymd[0] and answer[1] == ymd[1] and answer[2] > ymd[2]:
        answer = ymd
        save = info
        continue
print(*save)