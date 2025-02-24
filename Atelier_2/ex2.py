l1=[11, 45, 8, 23, 14, 12, 78, 45, 89]
morceaux = len(l1)//3
listEnMorc=[l1[i:i+morceaux] for i in range(0,len(l1),morceaux)]
print(listEnMorc)

reversed_List=[ele[::-1] for ele in listEnMorc]
print(reversed_List)