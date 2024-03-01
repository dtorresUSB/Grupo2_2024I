
def lectura(f):
    datos=f.readlines()
    mundial=[]
    for i in datos:
        mundial.append(i.rstrip('\n').split(','))
    return mundial

def campeon(datos):
    for elem in datos:
        if elem[12]=='Final':
            if elem[2]>elem[4] or elem[3]>elem[5]:
                print(elem[0])
            else:
                print(elem[1])

if __name__=="__main__":
    f=open('wcm.csv','r',encoding='utf8')
    datos=lectura(f)
    campeon(datos)
    print(datos[1])
    print(len(datos[1]))