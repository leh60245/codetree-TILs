n, k = map(int, input().split())
answer = dict()
for idx in range(1, n+1):
    input_string = input()
    answer[input_string] = str(idx)
    answer[str(idx)] = input_string

for _ in range(k):
    print(answer[input()])