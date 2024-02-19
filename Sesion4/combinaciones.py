from factorial import fcnFactorial as f

def main():
    n=int(input('Ingrese el numero de elementos: '))
    m=int(input('Ingrese el numero de grupos: '))
    comb=f(n)/(f(m)*f(n-m))
    print(f'Cantidad de combinaciones posibles: {comb}')

if __name__=="__main__":
    main()