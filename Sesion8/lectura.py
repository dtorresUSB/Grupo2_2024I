
def wholeFile(f):
    A=f.read().split('\n')
    B=[]
    for i in A:
        B.append(i.split(','))
    print(B[0][2])
    return B

def oneLine(f):
    A=f.readline().rstrip('\n').split(',')
    B=[]
    while A!=['']:
        A=f.readline().rstrip('\n').split(',')
        B.append(A)
    print(B[1][2])
    return B

def listFile(f):
    A=f.readlines()
    B=[]
    for i in A:
        B.append(i.rstrip('\n').split(','))
    print(B[3][3])
    return B

if __name__=="__main__":
    f=open('matrizAsignacion.txt','rt')
    #A=wholeFile(f)
    #A=oneLine(f)
    A=listFile(f)
    #f.seek(11)                 Ubicar el puntero
    print(A)
    print(type(A))