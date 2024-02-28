import random as rand

def main():
    rows=int(input('Ingrese el numero de filas: '))
    cols=int(input('Ingrese el numero de columnas: '))

    matriz=[]
    for i in range(rows):
        matriz.append([])
        for j in range(cols):
            matriz[i].append(rand.randint(0,100))
    for k in matriz:
        print(k)


if __name__=="__main__":
    main()