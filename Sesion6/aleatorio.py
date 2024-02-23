import random as rand

def main():
    lista=[]
    decimales=[]
    word=[]
    for i in range(10):
        n=rand.randint(0,10)
        d=round(rand.uniform(0,10),2)
        w=rand.choice('esternocleidomastoideo')
        word.append(w)
        decimales.append(d)
        lista.append(n)
    
    return lista,decimales,word

def sliding(listados):
    for i in listados:        #listados=([lista],[decimales],[word])
        for idx,val in enumerate(i):
            print(f'Indice: {idx}, valor: {val}')
        print('')
if __name__=="__main__":
    listados=main()
    sliding(listados)