n, k = map(int, input().split())
l = list(map(int, input().split()))

dit = dict()
for value in l:
    dit[value] = k - value

ans = 0
for value in l:
    if k - value in dit:
        ans += 1
        del dit[value]
        del dit[k-value]
        continue

print(ans)