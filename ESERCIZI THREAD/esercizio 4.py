# -*- coding: utf-8 -*-
"""
Created on Sat May 31 18:24:11 2025

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

def giocatori(palla):
    
    while palla is True:
        sleep(5)
        logging.info("colpo giocatore")
        pass


if __name__== "__main__":
    
    palla=True
    
    giocatore1=threading.Thread(target=giocatori, args=(palla,))
    
    giocatore2=threading.Thread(target=giocatori, args=(palla,))
    
    
    giocatore1.start()
    
    giocatore2.start()
    
    
    giocatore1.join()
    
    giocatore2.join()
      