def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
    
def sum_series(n, optional_one = 0, optional_two = 1):
    
    if optional_one == 2 and optional_two == 1:
        if n == 0:
            return 2
        if n == 1:
            return 1
        else:
            return sum_series(n-1,optional_one,optional_two) + sum_series(n-2,optional_one,optional_two)
    else:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return sum_series(n-1,optional_one,optional_two) + sum_series(n-2,optional_one,optional_two)

