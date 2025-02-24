x=int(input("Donner le nombre x : "))
n=int(input("Donner la puissance n : "))
puiss=0
for i in range(n):
    puiss+=x
print(f"la puissance de {x}**{n} est : {puiss}")