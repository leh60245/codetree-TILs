n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(m):
    b.append(list(map(int, input().split())))

a_point = 0
b_point = 0
now = ""
cnt = 0
while True:
    a_point += a[0][0]
    b_point += b[0][0]
    if a_point > b_point:
        if now != "A":
            cnt += 1
            now = "A"
    if a_point == b_point:
        if now != "AB":
            cnt += 1
            now = "AB"
    if a_point < b_point:
        if now != "B":
            cnt += 1
            now = "B"

    a[0][1] -= 1 
    b[0][1] -= 1
    if a[0][1]== 0:
        a.pop(0)
    if b[0][1] == 0:
        b.pop(0)
    
    if a != [] and b != []:
        continue
    break
print(cnt)