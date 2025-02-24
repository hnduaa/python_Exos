def apply_operation(a,b,funct):
    return funct(a,b)

def addition(a,b):
    return a+b

def multiplication(a,b):
    return a*b
print("la somme de 5+3 :",apply_operation(5,3,addition))
print("la multiplication de 5 x 3 :",apply_operation(5,3,multiplication))
