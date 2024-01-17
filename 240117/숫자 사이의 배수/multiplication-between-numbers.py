a, b = map(int, input().split())
arr = [i for i in range(a, b+1) if i % 5 == 0 or i % 7 == 0]
answer = sum(arr)
middle = len(arr)
print(f"{answer} {answer/middle:.1f}")