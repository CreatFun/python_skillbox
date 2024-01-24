import time


def validate_args(func):

    def wrapper(*args, **kwargs):
        args_count = len(args) + len(kwargs)
        if args_count < 1:
            return "Not enough arguments"
        if args_count > 1:
            return "Too many arguments"
        if not isinstance(args[0], int):
            return "Wrong types"
        if args[0] < 0:
            return "Negative argument"
        result = func(*args, **kwargs)
        return result

    return wrapper


def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        print(cache.values())
        return cache[n]

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} выполнялась {end_time - start_time:.6f} секунд")
        return result

    return wrapper


@validate_args
@memoize
def fibonacci_memoized(n):
    if n < 2:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


print("С мемоизацией: ")
fibonacci_memoized_timer = timer(fibonacci_memoized)(30)
print(fibonacci_memoized_timer)
fibonacci_memoized_timer = timer(fibonacci_memoized)(50)
print(fibonacci_memoized_timer)

print("===================")


@validate_args
def fibonacci_non_memoized(n):
    if n < 2:
        return n
    return fibonacci_non_memoized(n - 1) + fibonacci_non_memoized(n - 2)


print("Без мемоизации: ")
fibonacci_non_memoized_timer = timer(fibonacci_non_memoized)(30)
print(fibonacci_non_memoized_timer)
fibonacci_non_memoized_timer = timer(fibonacci_non_memoized)(33)
print(fibonacci_non_memoized_timer)
