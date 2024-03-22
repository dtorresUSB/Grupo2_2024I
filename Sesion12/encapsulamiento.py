class Estudiante:
    #----------------Constructor-----------
    def __init__(self):
        self.__nombre=None
        self.__codigo=None
        self.__carrera=None
        self.edad=20

    #----------------Getters---------------
    def getNombre(self):
        if self.edad>18:
          return self.__nombre
        else:
          print('Usted no es mayor de edad')
    
    def getCodigo(self):
        return self.__codigo
    
    def getCarrera(self):
        return self.__carrera
    
    def getHablar(self):
        return self.__hablar()
    
    #----------------Setters---------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre

    def setCodigo(self,codigo:int):
        if codigo<0:
            print('error en los datos')
        else:
            self.__codigo=codigo
    
    def setCarrera(self,carrera:str):
        self.__carrera=carrera

    #---------------Metodo----------------
    def __hablar(self):
        print(f'mi nombre es: {self.getNombre()} y mi codigo es {self.getCodigo()}')

    

def main():
    est1=Estudiante()
    est1.setNombre('Falcao')
    est1.setCodigo(263648)
    est1.getHablar()

if __name__=="__main__":
    main()