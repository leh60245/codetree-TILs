from sortedcontainers import SortedDict

sd = SortedDict()
n = int(input())
arr = list(map(int, input().split()))

for idx, value in enumerate(arr, start=1):
    if value not in sd:
        sd[value] = idx

print("\n".join([f"{k} {v}" for k, v in sd.items()]))