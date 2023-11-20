n = int(input())
arr = [0]
arrow = {"R":1, "L":-1}

p = 0
for _ in range(n):
    a, b = map(str, input().split())
    a = int(a)
    if b == "R":
        while a > 0 :
            arr[p] = arrow[b]
            a -= 1
            p += 1 if a > 0 else 0
            if p >= len(arr) and a > 0:
                arr.append(0)
    else:
        while a > 0 :
            arr[p] = arrow[b]
            a -= 1
            p -= 1  
            if p < 0:
                p += 1
                if a > 0 :
                    arr = [0] + arr
    
w = 0
b = 0
for i in arr:
    w += 1 if i == -1 else 0
    b += 1 if i == 1 else 0

print(w, b)