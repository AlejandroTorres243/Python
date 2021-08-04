# -*- coding: utf-8 -*-

from pymongo import MongoClient, ReturnDocument,DESCENDING

client = MongoClient("mongodb://localhost:27017/citas")
db=client.citas
users=db.usuarios
mensj=db.mensajes

print(users.count())
print(mensj.count())


print("Resultado ejercicio 2: ")
#    Ejercicio 2 Cómo puedo consultar todos los hombres con los ojos azules?
result = users.find({'sexo':"H", 'ojos':"azules"})
for item in result:
    print(item)
print("Resultado ejercicio 3: ")
#    Ejercicio 3 Dame mis últimos 10 mensajes como usuario enviados
result = mensj.find({'remitente':"Mabel"}, {'_id' :False}).limit(10).sort("fecha", DESCENDING)
for item in result:
    print(item)
print("Resultado ejercicio 4: ")
# Ejercicio 4 Dime mis 25 últimos mensajes recibidos ordenados descendientemente
result = mensj.find({'destinatario':"Mabel"}, {'_id' :False}).limit(25).sort("fecha", DESCENDING)
for item in result:
    print(item)

print("Resultado ejercicio 6: ")
#Ejercicio 6 Sentencia de cambio de contraseña de un usuario
result=users.find_one_and_update(
    {'nombre': "Donal"},
    {'$set': {'password': "5555"}},
    return_document=ReturnDocument.AFTER)
print( result)
print("Resultado ejercicio 7: ")
# Ejercicio 7 Sentencia de cambio de email de un usuario
result=users.find_one_and_update(
    {'nombre': "Donal"},
    {'$set': {'email': "donal@hotmail.com"}},
    return_document=ReturnDocument.AFTER)
print(result)

print("Resultado ejercicio 8:  ")
# Ejercicio 8: Activación de la cuenta de un usuario
result=users.find_one_and_update(
    {'nombre': "María"},
    {'$set': {'status': True}},
    return_document=ReturnDocument.AFTER)
print("Resultado ejercicio 8: ", result)


print("Resultado ejercicio 9:  ")
# Ejercicio 9 Dame todas las chicas mayores de 18 años que midan 179cm y pesen menos 120kg
result = users.find({
    'sexo':"M",
    'edad': {'$gt': 18},
    'altura':{'$gt':179},
    'peso': {'$lt': 120}
    }
)
for item in result:
    print(item)

print("Resultado ejercicio 10:  ")
# Ejercicio 10  Dame todos los chicos menores de 50 años que cobre más de 45000€ al año
result = users.find({
    'sexo':"H",
    'edad': {'$lt': 50},
    'salario':{'$gt':45000}
    }
)
for item in result:
    print(item)

print("Resultado ejercicio 11:  ")
# Ejercicio 11  Dame todas las mujeres sin hijos
result = users.find({
    'sexo':"M",
    'hijos':0,
    }
)
for item in result:
    print(item)

print("Resultado ejercicio 12:  ")
# Ejercicio 12  Dame todos los chicos que tengan un Audi
result = users.find({
    'sexo':"H",
    'coche':"Audi"
    }
)
for item in result:
    print(item)
