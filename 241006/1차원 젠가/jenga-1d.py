n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

tmp = []
for i in range(len(arr)):
    if (s1 - 1 <= i) and (i < e1):
        continue
    tmp.append(arr[i])
arr = tmp

tmp = []
for i in range(len(arr)):
    if (s2 - 1 <= i) and (i < e2):
        continue
    tmp.append(arr[i])

print(len(tmp))
for i in range(len(tmp)):
    print(tmp[i])