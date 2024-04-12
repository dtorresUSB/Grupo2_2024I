class Ciudadano():
    def __init__(self,idioma,nombre):
        self.__idioma=idioma
        self.__nombre=nombre

    def setIdioma(self,idioma):
        self.__idioma = idioma

    def setNombre(self,nombre):
        self.__nombre =nombre
    
    def getIdioma(self):
        return self.__idioma
    
    def getNombre(self):
        return self.__nombre
    
    # -------------- Sobrecarga ----------------
    def Saludo(self):
        print('Quoi de beau!')
    
class Colombia(Ciudadano):
    def __init__(self,idioma,nombre):
        super().__init__(idioma,nombre)
        self.CC=None
    
    def setCC(self,CC):
        self.CC = CC
    
    def getCC(self):
        return self.CC
    
    # -------------- Sobrecarga ----------------
    def Saludo(self):
        print('Qiubo pues home!')

class Inglaterra(Ciudadano):
    def __init__(self,idioma,nombre):
        super().__init__(idioma,nombre)
        self.Id=None
    
    def setId(self,Id):
        self.Id = Id
    
    def getId(self):
        return self.Id

    # -------------- Sobrecarga ----------------
    def Saludo(self):
        print("What's up bro!")

class China(Ciudadano):
    def __init__(self,idioma,nombre):
        super().__init__(idioma,nombre)
        self.Shengfenzheng=None

    def setShengfenzheng(self,Shengfenzheng):
        self.Shengfenzheng = Shengfenzheng
    
    def getShengfenzheng(self):
        return self.Shengfenzheng
    
    # -------------- Sobrecarga ----------------
    def Saludo(self):
        print('你干嘛呀!')

#---------------Funcion del polimorfismo--------------
def darSaludo(objeto):
    objeto.Saludo()
    

def main():

    while 1:
        print('Seleccione una de las siguientes paises: \n'\
            '1. Colombia\n'\
                '2. Inglaterra\n'\
                    '3. China\n'\
                        '4. Otro\n')
        pais=int(input('¿Cual es su nacionalidad?(Coloque un numero): '))
        idioma=input('¿Cual es su idioma?: ')
        nombre=input('¿Cual es su nombre?: ')

        paises=[Colombia,Inglaterra,China,Ciudadano]
        persona=paises[pais-1](idioma,nombre)
        print(f'Aplicante: {persona.getNombre()}, Idioma: {persona.getIdioma()}')
        darSaludo(persona)
        print('')
    

if __name__ == "__main__":
    main()