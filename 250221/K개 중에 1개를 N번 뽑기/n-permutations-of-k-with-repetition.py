K, N = map(int, input().split())

# Write your code here!

def permutation_with_multi(arr, lenght):
    result = []    
    def backtracking(v):
        if len(v) == lenght:
            result.append(v)
            print(*v)
            return
        for i in arr:
            backtracking(v+[i])
    backtracking([])
    return result

permutation_with_multi([i for i in range(1, K+1)], N)