
def main():
    meses=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago',
           'Sept','Oct','Nov','Dic']
    dias=['31','29','31','30','31','30','31','31',
           '30','31','30','31']
    festivos=['1ro enero y 6 reyes','29','20 dia de san jose',
              '30','31','30','31','31',
           'No hay','31','30','31']
    
    word=input('Ingrese un mes: ').capitalize()
    for idx,mes in enumerate(meses):
        if word==mes:
            print(f'el mes {mes} tiene {dias[idx]}')
            print(f'festivos: {festivos[idx]}')

if __name__=="__main__":
    main()
