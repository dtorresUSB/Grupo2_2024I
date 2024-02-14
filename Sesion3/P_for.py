#----------------- 1er ejercicio -------------
# decimal=0
# for i in range(10):
#     decimal+=0.5
#     print(decimal)

#----------------- 2do ejercicio -------------
# decimal=0
# for i in range(10):
#     decimal+=0.5
#     if decimal==2:
#         continue
#     print(decimal)

#----------------- 3er ejercicio -------------
num=int(input('Ingrese un numero: '))
txt='divisores=>(1'
for i in range(2,num+1):
    if num%i==0:
        txt+=','+ str(i)
print(f'{txt})')
