n = int(input())
count = 0
while True:
    if n % 2 == 0:
        n /= 2
    else:
        n *= 3
        n += 1
    count += 1
    if n == 1:
        print(count)
        break