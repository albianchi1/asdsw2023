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


def fattoriale(numero, numero_fine, risultati,indice):
    
    fattoriale=numero
    
    while numero > numero_fine:
        
        num=numero -1
        
        fattoriale =  fattoriale*num 
        
        numero=num
        
        logging.info(f"stampa {fattoriale} and {numero_fine}")
        
    risultati[indice]=fattoriale
        
        
if __name__ == "__main__":
    
    numero=100
    
    numero_thread=5
    
    risultati=[0,0,0,0,0]

    numero1=threading.Thread(target=fattoriale, args=(numero,80,risultati,0))
    
    numero1_2=threading.Thread(target=fattoriale, args=(79,60,risultati,1))
    
    numero1_3= threading.Thread(target=fattoriale, args=(59,40,risultati,2))
    
    numero1_4= threading.Thread(target=fattoriale, args=(39,20,risultati,3))
    
    numero1_5= threading.Thread(target=fattoriale, args=(19,1,risultati,4))
    
    numero1.start()
    
    numero1_2.start()
    
    numero1_3.start()
    
    numero1_4.start()
    
    numero1_5.start()
    
    numero1.join()
    
    numero1_2.join()
    
    numero1_3.join()
    
    numero1_4.join()
    
    numero1_5.join()
    
    risultato_finale=risultati[0]*risultati[1]*risultati[2]*risultati[3]*risultati[4]
    
    logging.info(f"stampa {risultato_finale}")