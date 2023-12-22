def fibonacci(N):
    if N == 0:
        return 0
    if N == 1:
        return 1

    if arr[N] != 0:
        return arr[N]

    arr[N] = fibonacci(N - 2) + fibonacci(N - 1)
    return arr[N]


N = int(input())

arr = [0] * (N + 1)

print(fibonacci(N))
