n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = -1
for start_i in range(n):
    for start_j in range(m):

        for end_i in range(start_i+1, n):
            for end_j in range(start_j+1, m):

                tmp = 0
                is_answer = True
                for i in range(start_i, end_i+1):
                    for j in range(start_j, end_j+1):
                        if arr[i][j] < 0:
                            is_answer = False
                            break
                    if is_answer is False:
                        break
                if is_answer:
                    ans = max(ans, (end_i-start_i+1) * (end_j-start_j+1))


print(ans)
