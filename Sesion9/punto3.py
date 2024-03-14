import random as r

def matriz():
    row=int(input('Ingrese n. filas: '))
    col=int(input('Ingrese n. columnas: '))
    a=[]

    for i in range(row):
        a.append([])
        for j in range(col):
            a[i].append(r.randint(-10,10))
        print(a[i])
    return a,row,col

def transpuesta(a,row,col):
    b=[]
    print('--------------')
    for i in range(col):
        b.append([])
        for j in range(row):
            b[i].append(a[j][i])
        print(b[i])

if __name__=="__main__":
    a,row,col=matriz()
    transpuesta(a,row,col)