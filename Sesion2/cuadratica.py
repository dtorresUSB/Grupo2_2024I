a=int(input('Ingrese el valor de a: '))
b=int(input('Ingrese el valor de b: '))
c=int(input('Ingrese el valor de c: '))

raiz=((b**2)-4*a*c)
x1=(-b+raiz**(1/2))/(2*a)
x2=(-b-raiz**(1/2))/(2*a)

if raiz<0:
    print('El resultado es imaginario')
else:
    print(f'Las raices reales son {x1} y {x2}')