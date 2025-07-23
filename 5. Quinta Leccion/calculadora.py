def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    if b == 0:
        raise ValueError('\nNo se puede dividir entre 0.\n')
    return a / b