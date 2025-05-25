# -*- coding: utf-8 -*-
"""
Created on Wed May 14 18:45:49 2025

@author: alber
"""

from multiprocessing import Process
from time import *
from random import *

#global value
#value=0


def sleeper(name,value):
    #global value
    local_value= str(value)
    t = gmtime()
    s = randint(4,10)
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' is going to sleep for ' + str(s) + ' seconds ' + 'with value: ' + local_value
    #+ str(value) 
    print(txt)
    #sleep(s)
    t = gmtime()
    txt = str(t.tm_min) + ':' + str(t.tm_sec) + ' ' + name + ' has woken up ' 
    #+ str(value)
    print(txt)
    
    
    
if __name__ == '__main__':
    process_list = list()
    #global value
    for i in range(3):
        p = Process(target=sleeper, args=('mike_{}'.format(i), i +1,))
        process_list.append(p)
        
        
    print('tutti pronti')
    
    
    for i, p in enumerate(process_list): 
        #value = i
        p.start()

    print('tutti avviati')
    
    
    for p in process_list: p.join()

    print('tutti terminati!')








