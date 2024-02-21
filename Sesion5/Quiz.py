def area(r):
    A=3.14*r**2
    return A

def volumen(r,h):
    V=area(r)*h
    return V

def main():
    r=int(input('Ingrese el radio: '))
    h=int(input('Ingrese la altura: '))

    print(f'El area es: {area(r)}')
    print(f'El volumen es: {volumen(r,h)}')



if __name__=="__main__":
    main()