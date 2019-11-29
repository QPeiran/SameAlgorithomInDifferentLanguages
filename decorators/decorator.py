def outer(some_func):
    def inner():
        print ("before some_func")
        reset = some_func
        n = reset + 1
        return n
    m = inner() + 2
    return m

def foo(k):
    return k+1
    
decorated = outer(foo(2))
print(decorated)
