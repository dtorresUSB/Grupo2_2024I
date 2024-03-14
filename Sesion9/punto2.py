
# def eliminar(a):
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#     print(b)

def eliminar(a):
    i=0
    j=1
    long=len(a)-1
    while i<(long):
        while j<(long):
            if a[i]==a[j]:
                a.pop(j)
            j+=1
            long=len(a)
        i+=1
        j=i+1
    print(sorted(a))

if __name__=="__main__":
    a=[5,4,1,4,8,4,3,2,5,6,1,2]
    eliminar(a)