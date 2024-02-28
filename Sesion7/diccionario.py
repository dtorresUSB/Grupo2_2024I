datos={'nombre':['Daniel','Juan','Mafe','Laura'],
       'codigo':[82738,83874,38472,23937],
       'carrera':'Ing. Mecatronica'}

cabecera=['nombre','codigo']
for idx,val in enumerate(datos):
    if val=='carrera':
        continue
    txt='Ingrese el '+cabecera[idx]+': '
    n=input(txt)
    datos[cabecera[idx]].append(n)

for i in range (len(datos['nombre'])):
    print(f'Estudiante: {datos['nombre'][i]}')
    print(f'Codigo: {datos['codigo'][i]}')
    print(f'Carrera: {datos['carrera']}\n')

