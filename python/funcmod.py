# Demo module, use:  "import funcmod" then say "funcmod.fibShow(x)" 

def fibShow(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
    
    
# stuff below this line is optional, but allows the code above to be run directly
# this can be used for testing

if __name__ == "__main__":    # then I've been run, not called from another module
    import sys
    fibShow(int(sys.argv[1]))
