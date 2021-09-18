# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:50:51 2021

@author: Manuel
"""

class America_sur():
    def cuentame(self):
        print('Paises de america del sur.')

class Argentina(America_sur):
    def aeropuerto_gg(self):
        print('Bienvenido a Argentina tio')
        
class Chile(Argentina):
    def aeropuerto_chill(self):
        print('Bienvenido weon a chile')
        
class Venezuela(Chile):
    def aeropuerto_oscuro(self):
        print('Bienvenido a Venezuela, cuidado por alli bb del paco')
        
class Colombia(Venezuela):
    def aeropuerto_quesero(self):
        print('Bienvenido a Colombia parsero peguese alli')
        
class Brasil(Colombia):
    def aeropuerto_do(self):
        print('bem-vindo ao brasil')
        
turista = Brasil()
turista.cuentame()
turista.aeropuerto_oscuro()
turista.aeropuerto_quesero()
turista.aeropuerto_chill()
turista.aeropuerto_gg()
turista.aeropuerto_do()
