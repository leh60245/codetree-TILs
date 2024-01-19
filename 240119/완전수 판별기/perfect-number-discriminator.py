n = int(input())
arr = []
for i in range(1,n):
    if n % i == 0:
        arr.append(i)
if sum(arr) == n:
    print("P")
else:
    print("N")