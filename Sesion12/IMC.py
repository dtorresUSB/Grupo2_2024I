
class Persona:
    #-------------Constructor----------
    def __init__(self):
        self.__nombre=None
        self.__altura=None
        self.__peso=None
        self.__edad=None
    
    #-------------Setters--------------
    def setNombre(self,nombre:str):
        self.__nombre=nombre
    
    def setAltura(self,altura:int):
        while altura<=0:
            print('La altura no puede ser menor a cero')
            altura=int(input('Ingrese la altura: '))
        self.__altura=altura

    def setPeso(self,peso:int):
        while peso<=0:
            print('El peso no puede ser menor a cero')
            peso=int(input('Ingrese la peso: '))
        self.__peso=peso

    def setEdad(self,edad:int):
        self.__edad=edad
    
    #-------------Getters--------------
    def getNombre(self):
        return self.__nombre
    
    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    def getEdad(self):
        return self.__edad
    
    #-------------Metodo-------------
    def IMC(self):
        calculo_imc=self.getPeso()/((self.getAltura()/100)**2)
        if calculo_imc<18.5:
            return 'Peso bajo'
        elif calculo_imc<24.9:
            return 'Saludable'
        elif calculo_imc<29.9:
            return 'sobrepeso'


def main():
    cliente=Persona()
    cliente.setNombre(input('Ingrese su nombre: '))
    cliente.setAltura(int(input('Ingrese la altura: ')))
    cliente.setPeso(int(input('Ingrese el peso: ')))
    print(f'Su IMC es: {cliente.IMC()}')

if __name__=="__main__":
    main()