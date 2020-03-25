# Fibonacci

# VERY BAD WAY OF DOING IT
def fib(n):
    if(n<=2):
        return 1
    table = {}
    a = 1
    b = 1
    c = 1

    for i in range(2, n):
        c = a+b
        a = b
        b = c
    return c


if __name__=="__main__":
    print(fib(10))
