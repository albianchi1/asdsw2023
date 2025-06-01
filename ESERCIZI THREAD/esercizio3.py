# -*- coding: utf-8 -*-
"""
Created on Sun May 25 11:35:52 2025

@author: alber
"""
import threading
import logging
import os
from time import sleep

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(threadName)s - %(process)d] %(message)s',
    datefmt='%H:%M:%S'
)



def produzione(lista_prodotti, soglia):
    
    #vedo se il thread di produzione ha superato una certa soglia
        
    while True:
        logging.info(f"dimensione p prodotti {len(lista_prodotti)}" )
        if len(lista_prodotti)< soglia:
            lista_prodotti.append("prodotto")
            logging.info("ho aggiunto un prodotto")
        sleep(5)
    
    
    
def consumo(lista_prodotti):
    #vedere se è presente almeno un prodotto da prelevare in magazzino
    while True:
        logging.info(f"dimensione c prodotti {len(lista_prodotti)}" )
        if len(lista_prodotti) >= 1:
            p=lista_prodotti.pop(0)
            logging.info("ho prelevato un prodotto")
        sleep(7)    
        

        
        

    
    
if __name__ == '__main__':
    
    lista_prodotti=[]
    soglia=5
    
    thread1 = threading.Thread(target=produzione, args=(lista_prodotti, soglia))
    thread2 = threading.Thread(target=consumo, args=(lista_prodotti,))
    
    
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    