personas={}
for i in range(3):
    n=input('Ingrese un nombre: ')
    if 'nombre' in personas:
        personas['nombre'].append(n)
    else:
        personas['nombre']=[n]
    print(personas)