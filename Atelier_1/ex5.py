def dectobin(x):
    if x == 0:
        return ''  
    else:
        return dectobin(x//2) + str(x%2)

def main():
    x=int(input('entrer la valeur x :'))
    if x==0:
        print("output : 0")
    else:
        print("output :" ,dectobin(x))

if __name__ == "__main__":
    main()