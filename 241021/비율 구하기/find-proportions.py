from sortedcontainers import SortedDict

sd = SortedDict()
n = int(input())

for _ in range(n):
    cmd = input()
    if cmd in sd:
        sd[cmd] += 1
    else:
        sd[cmd] = 1

print("\n".join([f"{k} : {v/n*100:.4f}" for k, v in sd.items()]))