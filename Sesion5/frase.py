word=input('Ingrese una frase: ')
idx=int(input('Indique una posicion: '))
print(f'En la posicion {idx} encontrará: {word[idx]}')
print(f'Longitud {len(word)}')

for i in range(len(word)):
    print(word[i])