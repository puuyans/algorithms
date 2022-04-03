# An example of an O(2^n) function is the recursive calculation of Fibonacci numbers. O(2^n) denotes an algorithm whose
# growth doubles with each addition to the input data set



def fibonacci(n):
    if n < 0:
        return "invalid input"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))
