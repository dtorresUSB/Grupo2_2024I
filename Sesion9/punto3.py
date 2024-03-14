import random as r

def matriz():
    row=int(input('Ingrese n. filas: '))
    col=int(input('Ingrese n. columnas: '))
    a=[]

    for i in range(row):
        a.append([])
        for j in range(col):
            a[i].append(r.randint(-10,10))
    return a,row,col

def transpuesta(a,row,col):
    b=[]

    for i in range(col):
        b.append([])
        for j in range(row):
            b[i].append(a[j][i])
    
    for i in a:
        print(i)
    print('--------------')
    for i in b:
        print(i)

if __name__=="__main__":
    a,row,col=matriz()
    transpuesta(a,row,col)