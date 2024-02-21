milista=['Hola',23,45.3,True]
# idx=input('Ingrese una posicion: ')

# while idx.lower()!='salir':
#     print(milista[int(idx)])
#     idx=input('Ingrese una posicion: ')

for i in milista:
    print(i)

for i in range(len(milista)):
    print(milista[i])

for idx,val in enumerate(milista):
    print(f'Elemento indice #{idx}= {val}')