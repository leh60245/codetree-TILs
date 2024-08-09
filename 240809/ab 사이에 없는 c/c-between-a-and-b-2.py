a, b, c = map(int, input().split())
while True:
    if b < c:
        print("YES")
        break
    if a <= c and c <= b:
        print("NO")
        break
    c += c