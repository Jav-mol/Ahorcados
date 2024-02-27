import json, random, os, time, sys
from source.logs.logger import logging


class Palabra:
    def __init__(self) -> None:
        self.palabra = self.palabra_aleatoria()

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

if __name__ == '__main__':
    x = Vidas()
    print(x.dificultad())
    