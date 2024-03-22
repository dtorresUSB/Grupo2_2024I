
class Estudiante:
    def __init__(self):
        self.nombre=None
        self.codigo=None
        self.carrera=None
        self.universidad=None

    def entender(self):
        print(f'yo {self.nombre} Entendí perfectamente :D')

def main():
    est1=Estudiante()
    est1.nombre="Falcao Garcia"
    est1.codigo=2893789214
    est1.carrera="Deportes"
    est1.universidad="La Salle"
    print(f'mi nombre es {est1.nombre} con codigo {est1.codigo}\n'
          f'Estudio {est1.carrera} en la u {est1.universidad}')
    
    est2=Estudiante()
    est2.nombre="Jhonny Bravo"
    est2.codigo=2348973
    est2.carrera="Modelo"
    est2.universidad="de modelaje"
    print(f'mi nombre es {est2.nombre} con codigo {est2.codigo}\n'
          f'Estudio {est2.carrera} en la u {est2.universidad}')

    print('------------------------------------------------')
    print(id(est1))
    print(est1.nombre)
    est1.nombre='Victor Ortega'
    print(id(est2))
    est3=Estudiante()
    print(id(est3))
    print(est3.nombre)

    print('------------------------------------------------')
    est1.entender()
    est2.entender()

if __name__=="__main__":
    main()