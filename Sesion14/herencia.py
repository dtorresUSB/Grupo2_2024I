

class Deportista:
    #-------------Constructor---------------
    def __init__(self,nombre:str,documento:int,edad:int):
        self.__nombre=nombre
        self.__documento=documento
        self.__edad=edad

    #------------- Setters -----------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    def setDocumento(self,documento:int):
        self.__documento=documento
    def setEdad(self,edad:int):
        self.__edad=edad

    #---------------Getters----------------
    def getNombre(self):
        return self.__nombre
    def getDocumento(self):
        return self.__documento
    def getEdad(self):
        return self.__edad
    
    #-----------Sobrecarga------------
    def deporte(self):
        return 'Es deportista'
    
class DeportistaTenis(Deportista):
    def __init__(self, nombre: str, documento: int, edad: int,
                 sg:int,sp:int):
        super().__init__(nombre, documento, edad)
        self.__setsGanados=sg
        self.__setsPerdidos=sp

    def setGanados(self,SG:int):
        self.__setsGanados=SG
    def setPerdidos(self,SP:int):
        self.__setsPerdidos=SP

    def getGanados(self):
        return self.__setsGanados
    def getPerdidos(self):
        return self.__setsPerdidos
    
    def ACE(self):
        return('Yo soy deportista de Tenis')
    
    #-----------Sobrecarga------------
    def deporte(self):
        return 'Tenis'
    
    def info(self):
        return f'Sets ganados: {self.getGanados()}\n'\
        f'Sets perdidos: {self.getPerdidos()}'

class DeportistaBasket(Deportista):
    def __init__(self, nombre: str, documento: int, edad: int,
                 equipo:str,cesta:int):
        super().__init__(nombre, documento, edad)
        self.__nombreEquipo=equipo
        self.__cestas=cesta

    def setNombreEquipo(self,equipo:str):
        self.__nombreEquipo=equipo
    def setCestas(self,cestas:int):
        self.__cestas=cestas

    def getNombreEquipo(self):
        return self.__nombreEquipo
    def getCestas(self):
        return self.__cestas
    
    def anotar(self):
        return('Yo soy deportista de basket')
    
    #-----------Sobrecarga------------
    def deporte(self):
        return 'Basket'
    
    def info(self):
        return f'Equipo: {self.getNombreEquipo()}\n'\
        f'# de puntos: {self.getCestas()}'

class DeportistaFutbol(Deportista):
    def __init__(self, nombre: str, documento: int, edad: int,
                 equipo:str,goles:int):
        super().__init__(nombre, documento, edad)
        self.__nombreEquipo=equipo
        self.__goles=goles

    def setNombreEquipo(self,equipo:str):
        self.__nombreEquipo=equipo
    def setGoles(self,goles:int):
        self.__goles=goles

    def getNombreEquipo(self):
        return self.__nombreEquipo
    def getGoles(self):
        return self.__goles
    
    def patear(self):
        return('Yo soy deportista de futbol')
    
    #-----------Sobrecarga------------
    def deporte(self):
        return 'Futbol'
    
    def info(self):
        return f'Equipo: {self.getNombreEquipo()}\n'\
        f'# de goles: {self.getGoles()}'

def datos():
    print('Escriba una de las siguientes opciones\n'
          '1. Futbol.\n','2. Basket\n','3. Tenis\n')
    opc=input('Escoja un deporte: ')
    nombre=input('Ingrese un nombre: ')
    documento=int(input('Ingrese un Documento: '))
    edad=int(input('Ingrese un Edad: '))
    return opc,nombre,documento,edad

def main():
    listado=[]
    data=datos()

    while data[0]!='exit':
        if data[0]=='Futbol':
            equipo=input('Ingrese el equipo: ')
            goles=int(input('Ingrese el # de goles: '))
            jugador=DeportistaFutbol(data[1],data[2],data[3],equipo,goles)
            print(jugador.patear())
            listado.append(jugador)
        elif data[0]=='Basket':
            equipo=input('Ingrese el equipo: ')
            cesta=int(input('Ingrese el # de puntos: '))
            jugador=DeportistaBasket(data[1],data[2],data[3],equipo,cesta)
            print(jugador.anotar())
            listado.append(jugador)
        elif data[0]=='Tenis':
            sg=input('Ingrese el de sets ganados: ')
            sp=int(input('Ingrese el de sets perdidos: '))
            jugador=DeportistaTenis(data[1],data[2],data[3],sg,sp)
            print(jugador.ACE())
            listado.append(jugador)

        print('----Listado de jugadores------\n')
        for idx,val in enumerate(listado):
            print(f'---------Jugador {idx+1}---------')
            print(f'{idx+1}: {val.getNombre()} deporte:{val.deporte()}')
            print('------datos del jugador------')
            print(f'documento:{val.getDocumento()}')
            print(f'edad:{val.getEdad()}')
            print('----------------------------------')
            print(val.info())
            print('---------------------------------\n')
        print('')
        #print(listado)
        data=datos()


if __name__=="__main__":
    main()
