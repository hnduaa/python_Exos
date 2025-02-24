l =[11, 45, 8, 11, 23, 45, 23, 45, 89]
dict={}
tmp=0
for ele in l :
    for i in range(len(l)) :
        if ele == l[i] :
            tmp+=1
    dict[ele]=tmp
    tmp = 0

print(dict)
