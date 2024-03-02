import json, random, os, time, sys
from source.logs.logger import logging
from source.diagramas import *

class Palabra:
    
    def palabra_aleatoria(self):
        
        with open('source/palabras.json') as file:
            
            word_json = json.load(file)
            palabra_aleatoria = random.choice(word_json)
            
            return palabra_aleatoria.lower()

options = """Seleccione la dificultad:
1-Facil > Vidas:15
2-Medio > Vidas:10
3-Dificil > Vidas:5
0-Quit
=> """  

class Vidas:
    def dificultad(self):  
        while True:
            try: 
                print(' AHORCADOS '.center(25,'-'))
                option = int(input(options))   
                
                if option == 1:
                    vidas = 15
                    break
                elif option == 2:
                    vidas = 10
                    break
                elif option == 3:
                    vidas = 5
                    break
                elif option == 0:
                    vidas = None
                    break
                else:
                    print('Ingrese una opcion valida')
                    time.sleep(1)
                    os.system('clear')
            except Exception as e:
                print('Ingrese una opcion valida')
                time.sleep(1)    
                os.system('clear') 
                logging.debug(f'Error: {e}')
                        
        if not vidas:
            sys.exit()  
                          
        os.system('clear')
        return vidas

class Diagramas:
    def __init__(self, dificultad) -> None:
        self.dificultad = dificultad
        
    def graficos(self):
        if self.dificultad == 15:
            return facil        
        elif self.dificultad == 10:
            return medio
        elif self.dificultad == 5:
            return dificil
    
    def diagramas(self, vidas):
        grafico = self.graficos()
        print(''.center(35,'~'))
        print(grafico.get(vidas, ''))
            
if __name__ == '__main__':
    try:
        pass
    except Exception as e:
        print(f'Error: {e}')
    