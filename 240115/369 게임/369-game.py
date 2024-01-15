n = int(input())
for i in range(1, n+1):
    if i % 3 == 0:
        print("0", end=" ")
        continue
    elif "3" in str(i) or "6" in str(i) or "9" in str(i):
        print("0", end=" ")
        continue
    else:
        print(i, end=" ")