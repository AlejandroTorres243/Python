# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:29:33 2021

@author: Manuel
"""

class Conder():
    def __init__(self):
        self.name = input('Name_')
        self.lang = input('Languages_')
    def sho_details(self):
        print('Name:'+ str(self.name) + '/Language:' + str(self.lang))
    
class Pythonner():
    def __init__(self):
        self.profile = Conder()
    def profiles(self):
        self.profile.sho_details()
        
active = Conder()
active.sho_details()

python = Pythonner()
python.profiles()