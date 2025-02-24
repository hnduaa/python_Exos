def char_freq(x,y):
    return str(x).count(y)

def main():
    x=input('entrer la chaine :')
    y=input('entrer le caractere :')
    print("output :" ,char_freq(x,y))

if __name__ == "__main__":
    main()