def fib(index):
    if index in {0, 1}:
        return index
    else:
        return fib(index-1) + fib(index-2)


print([fib(i) for i in range(10)][::-1])
