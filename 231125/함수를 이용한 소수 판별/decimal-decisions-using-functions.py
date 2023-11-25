a, b = map(int, input().split())


def foo(a, b):
    arr = [2]
    for i in range(3, b+1):
        p = True
        for j in arr:
            if i % j == 0:
                p = False
                break
        if p:
            arr.append(i)
    answer = [i if i >= a and i <= b else 0 for i in arr]
    print(sum(answer))

foo(a, b)