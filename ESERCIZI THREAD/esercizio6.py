# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 16:03:42 2025

@author: alber
"""

from multiprocessing import Process 
from time import sleep
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(threadName)s - %(process)d] %(message)s',
    datefmt='%H:%M:%S'
)


def file_estension(file,cartella,sottocartella):
    
    while file in sottocartella:
        while sottocartella in cartella:
            logging.info(f"stampa {file} and {sottocartella}")
            sleep(10)


if __name__=='__main__':
    
    
    
    p=Process(target=file_estension, args=(file,cartella,sottocartella))
    