n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

arr = arr[:s1-1] + arr[e1-1:]
tmp = arr[:s1-1] + arr[e1-1:]

print(len(tmp))
for i in range(len(tmp)):
    print(tmp[i])