def agregar(x):
    n=input('Ingrese un valor: ')
    x.append(n)
    print(x)
    return x

def remover(x):
    n=input('Ingrese un valor: ')
    x.remove(n)
    print(x)
    return x

def main():
    milista=[]
    print('1. Agregar\n2. Remover\n')
    opc=input('Escoja una de las opciones: ')

    while opc!='salir':
        if opc=='1':
            milista=agregar(milista)
        elif opc=='2':
            milista=remover(milista)
        opc=input('Escoja una de las opciones: ')


if __name__=="__main__":
    main()