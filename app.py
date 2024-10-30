def check(a):
    if not (isinstance(a, float) or isinstance(a, int)):
        raise ValueError("Please, enter digits.")

def square(a):
    check(a)
    a_int = int(a)
    if a-a_int==0:
       return a_int ** 2 
    return a ** 2

def cube(a):
    check(a)
    a_int = int(a)
    if a-a_int==0:
       return a_int ** 3 
    return a ** 3