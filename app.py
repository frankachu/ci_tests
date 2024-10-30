def check(a):
    if not (isinstance(a, float) or isinstance(a, int)):
        raise ValueError("Please, enter digits.")

def square(a):
    check(a)
    return a ** 2

def cube(a):
    check(a)
    return a ** 3