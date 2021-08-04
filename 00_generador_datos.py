# -*- coding: utf-8 -*-

from pymongo import MongoClient, ReturnDocument,DESCENDING, ASCENDING
from random import randint
import datetime

client = MongoClient("mongodb://localhost:27017/citas")
db=client.citas
users=db.usuarios
mensj=db.mensajes

# Generar usuarios
# Resolución de ejercicio 5
maria= users.insert_one({'nombre':"María", 'password':"1234", 'email':"maria@mail.com", 'altura':156, 'peso':60, 'edad':27, 'ojos':"azules", 'sexo':"M"})
users.create_index([("nombre",DESCENDING)],unique=True)
esti= users.insert_one({'nombre':"Esti", 'password':"1234", 'email':"esti@mail.com", 'altura':180, 'peso':60, 'edad':30, 'ojos':"marrones", 'sexo':"M"})
mabel= users.insert_one({'nombre':"Mabel", 'password':"1564", 'email':"mabel@mail.com", 'altura':166, 'peso':70, 'edad':40, 'ojos':"azules", 'sexo':"M"})
pepe= users.insert_one({'nombre':"Pepe", 'password':"1256", 'email':"pepe@mail.com", 'altura':190, 'peso':80, 'edad':35, 'ojos':"verdes", 'sexo':"H"})
juan= users.insert_one({'nombre':"Juan", 'password':"1234", 'email':"juan@mail.com", 'altura':170, 'peso':70, 'edad':27, 'ojos':"azules", 'sexo':"H"})
donal= users.insert_one({'nombre':"Donal", 'password':"1234", 'email':"donal@mail.com", 'altura':178, 'peso':70, 'edad':34, 'ojos':"azules", 'sexo':"H"})
david= users.insert_one({'nombre':"David", 'password':"1984", 'email':"david@mail.com", 'altura':170, 'peso':80, 'edad':40, 'ojos':"verdes", 'sexo':"H"})
ana=users.insert_one({'nombre':"Ana",'password':"1234",'email':"ana@mail.com",'altura':180,'peso':115,'edad':20,'ojos':"marrones",'sexo':"M"})

nombre = ['Donal', 'Esti', 'Mabel', 'Pepe','Juan', 'María', 'David', 'Ana']
texto = ['Hola', 'Buenas', 'Hello']
fecha = [datetime.datetime(2018, 9, 8, 18, 17, 28, 324000),datetime.datetime(2018, 7, 8, 18, 17, 28, 324000),datetime.datetime(2017, 7, 8, 18, 17, 28, 324000)]


#Selecciona la coleccion mensj
#mensj
for x in range(1, 51):
    remitente=nombre[randint(0, (len(nombre)-1))]
    destinatario=nombre[randint(0, (len(nombre)-1))]
    if(remitente==destinatario):
        remitente=nombre[randint(0, (len(nombre)-1))]
    #Creo el objeto que quiero insertar
    business = {
        'remitente' : remitente,
        'destinatario' : destinatario,
        'text' : texto[randint(0, (len(texto)-1))],
        'fecha': fecha[randint(0, (len(fecha)-1))]
    }
    #Step 3: Insert business object directly into MongoDB via insert_one
    result=mensj.insert_one(business)
    #Step 4: Print to the console the ObjectID of the new document
    print('Creado nº {0} de 50 con el ID:{1}'.format(x,result.inserted_id))