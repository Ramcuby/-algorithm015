def fib(n):
    a = [0 for _ in range(n+1)]
    a[0],a[1] = 0,1
    for i in range(2,n+1):
        a[i] = a[i-2] + a[i-1]
    return a[n]

print(fib(5))