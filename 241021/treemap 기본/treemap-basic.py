from sortedcontainers import SortedDict

sd = SortedDict()

n = int(input())

for _ in range(n):
    cmd = input()
    if cmd.startswith("add"):
        _, k, v = cmd.split()
        sd[int(k)] = v
    elif cmd.startswith("remove"):
        _, k = cmd.split()
        del sd[int(k)]
    elif cmd.startswith("find"):
        _, k = cmd.split()
        if int(k) in sd:
            print(sd[int(k)])
        else:
            print(None)
    else:
        if not sd == {}:
            print(" ".join([v for _, v in sd.items()]))
        else:
            print(None)