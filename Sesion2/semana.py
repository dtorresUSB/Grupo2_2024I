dia=input('Ingrese un dia de la semana: ').capitalize()
if dia=='Lunes':
    n='el 1er'
elif dia=='Martes':
    n='el 2do'
elif dia=='Miercoles':
    n='el 3er'
elif dia=='Jueves':
    n='el 4to'
elif dia=='Viernes':
    n='el 5tr'
elif dia=='Sabado':
    n='el 6to'
elif dia=='Domingo':
    n='el 7mo'
else:
    n='No es un'    
print(f'{n} dia de la semana')
