import os, time
from source.palabra import Palabra, Vidas

titulo = f"{''.center(35,'~')}\n{'AHORCADOS '.center(35,'-')}"

class Ahorcados:
    
    def __init__(self) -> None:
            self.palabra = Palabra().palabra_aleatoria()
            self.vidas = Vidas().dificultad()
            self.palabra_final = ''
            
    def menu(self):
        os.system('clear')     
        print(titulo)
        print(f"Palabra: {self.palabra_final} | Vidas: {self.vidas}")         
        letra = input("Ingrese una letra: ").lower()          
        return letra
    
    def ganador(self):
        os.system('clear')     
        print(titulo)
        print(f'Ganaste | Vidas: {self.vidas} - Palabra: {self.palabra_final} \n{"".center(35,"~")}')
        
    def perdedor(self, end, count, word):
        os.system('clear')     
        print(titulo)
        print(f'Perdiste: {end} - {word} | Vidas: {count}')
    
    def ahorcados(self):
        resul = list("_"*len(self.palabra))    
        while True:
            if self.palabra_final == self.palabra:
                self.ganador()
                return
                                   
            if self.vidas < 1:
                self.perdedor(self.palabra_final, self.vidas, self.palabra)
                break
                    
            letra_input = self.menu() 
            if letra_input not in self.palabra:
                self.vidas -= 1
                print(' Prueba con otra letra '.center(35,'-'))
                time.sleep(1)
                continue
            
            for indice, letra in enumerate(self.palabra):
                if letra == letra_input:
                    resul[indice] = letra 
                    self.palabra_final = "".join(resul)
