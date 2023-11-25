n = int(input())

def foo(year):
    if year % 400 == 0:
        return print("true")
    if year % 100 == 0:
        return print("false")
    if year % 4 == 0:
        return print("true")
    return print("false")

foo(n)