def fact(x):
    if x==0 | x==1 :
        return 1
    else:
        return x*fact(x-1)

x=int(input("Donner le nombre x : "))
print(f"Le fact de {x} est : {fact(x)}")