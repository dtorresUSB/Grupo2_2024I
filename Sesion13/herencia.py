
class Deportista:
    #------------ Constructor -------------
    def __init__(self,datos):
        self.__nombre=datos[0]
        self.__edad=datos[1]
        self.__Documento=datos[2]

    #------------ Setters ----------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setEdad(self,edad:int):
        self.__edad=edad
    def setDocumento(self,documento:str):
        self.__Documento=documento
    
    #------------ Getters ----------------
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getDocumento(self):
        return self.__Documento
    
    #------------sobrecarga----------------
    def medalla(self):
        return f'Yo soy deportista campeon'

class DeportistaTenis(Deportista):
    def __init__(self,datos):
        super().__init__(datos)
        self.__setGanados=None
        self.__setPerdidos=None
    
    def setGanados(self,SG:int):
        self.__setGanados=SG
    def setPerdidos(self,SP:int):
        self.__setPerdidos=SP

    def getGanados(self):
        return self.__setGanados
    def getPerdidos(self):
        return self.__setPerdidos
    
    def Ace(self):
        return f'Yo {self.getNombre()} soy jugador de Tenis'
    
    #------------sobrecarga----------------
    def medalla(self):
        return f'Yo soy deportista campeon de tenis'

class DeportistaFutbol(Deportista):
    def __init__(self):
        super().__init__()
        self.__NombreEquipo=None
        self.__goles=None
    
    def setEquipo(self,equipo:str):
        self.__NombreEquipo=equipo
    def setGoles(self,goles:int):
        self.__goles=goles

    def getEquipo(self):
        return self.__NombreEquipo
    def getGoles(self):
        return self.__goles
    
    def Anotar(self):
        return f'Yo {self.getNombre()} soy jugador de Futbol'
    
    #------------sobrecarga----------------
    def medalla(self):
        return f'Yo soy deportista campeon Futbol'

class DeportistaBasket(Deportista):
    def __init__(self):
        super().__init__()
        self.__NombreEquipo=None
        self.__cestas=None
    
    def setEquipo(self,equipo:str):
        self.__NombreEquipo=equipo
    def setCestas(self,cestas:int):
        self.__cestas=cestas

    def getEquipo(self):
        return self.__NombreEquipo
    def getCestas(self):
        return self.__cestas
    
    def Encestar(self):
        return f'Yo {self.getNombre()} soy jugador de Basket'

def registro():
    nombre=input('Ingrese el nombre: ')
    edad=input('Ingrese la edad: ')
    documento=input('Ingrese un documento: ')
    return nombre,edad,documento

def main():
    listado=[]
    print('Escoja un deporte: \n'
          '1. Tenis\n'
          '2. Futbol\n'
          '3. Basket\n')
    opc=input('Seleccione un deporte: ')

    while opc!='exit':
        if opc=='Tenis':
            datos=registro()
            jugador=DeportistaTenis(datos)
            print(jugador.Ace())
            print(jugador.medalla())
            listado.append(jugador)
        elif opc=='Futbol':
            datos=registro()
            jugador=DeportistaFutbol()
            jugador.setNombre(datos[0])
            jugador.setDocumento(datos[2])
            jugador.setEdad(datos[1])
            print(jugador.Anotar())
            print(jugador.medalla())
            listado.append(jugador)
        elif opc=='Basket':
            datos=registro()
            jugador=DeportistaBasket()
            jugador.setNombre(datos[0])
            jugador.setDocumento(datos[2])
            jugador.setEdad(datos[1])
            print(jugador.Encestar())
            print(jugador.medalla())
            listado.append(jugador)
        else:
            print('error en la seleccion')
        print(listado)
        print('Escoja un deporte: \n'
          '1. Tenis\n'
          '2. Futbol\n'
          '3. Basket\n')
        opc=input('Seleccione un deporte: ')
        

if __name__=="__main__":
    main()