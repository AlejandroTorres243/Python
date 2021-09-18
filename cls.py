# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 15:31:30 2021

@author: Manuel
"""

class LenVal():
    def __init__(self,value):
        self.lista = value
        self.sho_val = len(value)
    def sho_val(self):
        print(self.lista)
    def sho_val2(self):
        print('tam:' +str(len(self.lista)))
lista = LenVal([1,9,4,2,6])
print(lista.sho_val)
