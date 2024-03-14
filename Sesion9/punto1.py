
def palindromo():
    txt=input('Ingrese una frase: ').lower()
    txt2=''
    for i in txt:
        if i!=' ':
            txt2+=i
    print(txt2)

    for i in range(len(txt2)//2):
        if txt2[i]!=txt2[-(i+1)]:
            print('no es palindromo')
            return
    print('si es palindromo')

if __name__=="__main__":
    palindromo()