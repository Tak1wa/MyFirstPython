import sys
from mymodule import fact, fib

print(sys.version)
print("factorial of 3 is {0}".format(fact(3)))

for n in range(7):
    print("fib({0}) is {1}".format(n, fib(n)))
