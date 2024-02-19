def tabular(x):
    
    txt=''
    for i in range(x):
        y=5*(i**2)+3*i-2
        txt+=str(y)+' '
    print(txt)
    print(f'nombre2{__name__}')

if __name__=="__main__":
    tabular(8)