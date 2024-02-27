from source.ahorcados import Ahorcados
from source.logs.logger import logging

if __name__=='__main__':
    try:
        logging.debug(f'Inicio del juego')
        
        Ahorcados().ahorcados()
        
        logging.debug(f'Fin del juego')
        
    except Exception as e:
        logging.error(f'Error: {e}')
        print(e)