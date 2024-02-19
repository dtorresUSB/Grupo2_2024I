#--------Funcion con parámetros--------
def operacion(a,b):
    c=a+b
    d=a-b
    return c,d

#--------Funcion sin parámetros--------
def imprimir():
    print('Operacion exitosa...')

n1=int(input('Ingrese un numero: '))
n2=int(input('Ingrese un numero: '))
imprimir()
sumar,restar=operacion(n1,n2)
print(f'Suma:{sumar}, resta:{restar}')