def agregar(x):
    n=input('Ingrese un valor: ')
    x.append(n)
    return x

def remover(x):
    n=input('Ingrese un valor: ')
    x.remove(n)
    return x

def insertar(x):
    idx=int(input('Ingrese el indice: '))
    n=input('Ingrese un valor: ')
    x.insert(idx,n)
    return x

def clear(x):
    x.clear()
    return x

def main():
    milista=['4','5','1']
    print('1. Agregar\n2. Remover\n')
    opc=input('Escoja una de las opciones: ')

    while opc!='salir':
        if opc=='1':
            milista=agregar(milista)
        elif opc=='2':
            milista=remover(milista)
        elif opc=='3':
            milista=insertar(milista)
        elif opc=='4':
            milista=clear(milista)
        print(milista)
        opc=input('Escoja una de las opciones: ')


if __name__=="__main__":
    main()