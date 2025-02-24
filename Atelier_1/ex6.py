def nombchiff(x) :
    if not isinstance(x, int) :
        return ''
    if x == 0:
        return 0
    else :
        return 1 + nombchiff(x // 10) 
x=int(input('entrer la valeur x :'))
print(f"Nombre de chiffre dans {x} est : {nombchiff(x)}")
