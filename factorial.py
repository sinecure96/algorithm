def factorial(N):
    ans = 1
    while N > 0:
        ans = ans * N
        N -= 1
    return ans

n = int(input())

print(factorial(n))