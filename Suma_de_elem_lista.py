# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 13:09:03 2021

@author: Manuel
"""

class Sum_list():
    def __init__(self, lst):
        self.List = lst
        self.List_len = len(lst)
        self.l1 = 0
        self.l2 = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.l2 == self.List_len:
            raise StopIteration
        else:
            self.sum_posit = self.List[self.l1] + self.List[self.l2]
            self.l1 += 1
            self.l2 += 1
            return self.sum_posit

lista = Sum_list([20,51,77,44,99,241])

for elem in lista:
    print(elem)