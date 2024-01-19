n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(f"{sum(arr)} {sum(arr)/len(arr):.1f}")