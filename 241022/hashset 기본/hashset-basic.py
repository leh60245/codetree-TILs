n = int(input())
hs = set()

for _ in range(n):
    cmd = input()
    if cmd.startswith("add"):
        _, v = cmd.split()
        hs.add(v)
    elif cmd.startswith("remove"):
        _, v = cmd.split()
        hs.remove(v)
    elif cmd.startswith("find"):
        _, v = cmd.split()
        if v in hs:
            print('true')
        else:
            print('false')