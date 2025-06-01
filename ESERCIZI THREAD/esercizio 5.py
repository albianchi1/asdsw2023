# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 12:35:44 2025

@author: alber
"""

import threading
import logging
from time import sleep


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(threadName)s - %(process)d] %(message)s',
    datefmt='%H:%M:%S'
)


def fattoriale(numero_grande):
    
    while numero_grande != 0:
        
        numero_grande=numero_grande%2
        
        logging.info(f"stampa numero {numero_grande}")
        
        sleep(5)
        
if __name__ == "__main__":
    
    numero_grande=40

    numero1=threading.Thread(target=fattoriale, args=(numero_grande,))
    
    numero1.start()
    
    numero1.join()