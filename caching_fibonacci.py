def caching_fibonacci():
    cache = {}
    
    def fibonacci(n):
        if n < 0:
            return 0
        if n == 1:
            return 1
        
        if n in cache:
            print(f"Fetching from cache: {n}")
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        print(f"Calculating fibonacci({n}) = {cache[n]}")
        return cache[n]
    
    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(5))
print(fib(7))
print(fib(8))