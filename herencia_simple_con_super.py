# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:01:41 2021

@author: Manuel
"""

# Diferencia entre variable con _ y con __ en una clase
# variable X = publica
# variable con _ = static
# variable con __ = private

class Number():
    def __init__(self):
        self.num = 0
    def increment(self):
        self.num += 1
    def decrement(self):
        self.num -= 1
     
class New_number(Number):
    def __init__(self):
        #SUPER: llamada de clase padre
        super().__init__()
    def sho_val(self):
        print('Value:'+str(self.num))
        
number = New_number()
number.increment()
number.increment()
number.increment()
number.decrement()
number.sho_val()