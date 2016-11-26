def fact(n):
    if(n <= 1):
        return 1
    else:
        return n * fact(n-1)

def fib(n):
    if(n < 0):
        return -1
    elif(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fib(n-2) + fib(n-1)