# -*- coding: utf-8 -*-
from bson.objectid import ObjectId
from pymongo import MongoClient, ReturnDocument
from random import randint


client = MongoClient("mongodb://localhost:27017/citas")
db=client.citas
users=db.usuarios


# Ejercicio 8: hacer que todos los usuarios tengan el campo 'status'
result = users.find({})
#activado = [True,False]
activado = [False]
for item in result:
    active = activado[randint(0, (len(activado) - 1))]
    users.find_one_and_update(
        {
            '_id': ObjectId(item.get('_id'))
        },
        {
            '$set': {'status': active}
        }
    )
# Ejercicio 10: hacer que todos los usuarios tengan el campo 'salario'
result = users.find({})
salarios = [10000,70000,50000]
for item in result:
    salario = salarios[randint(0, (len(salarios) - 1))]
    users.find_one_and_update(
        {
            '_id': ObjectId(item.get('_id'))
        },
        {
            '$set': {'salario': salario}
        }
    )

# Ejercicio 11: hacer que todos los usuarios tengan el campo 'hijos'
result = users.find({})
hijos = [0,1,2,3,4]
for item in result:
    hijo = hijos[randint(0, (len(hijos) - 1))]
    users.find_one_and_update(
        {
            '_id': ObjectId(item.get('_id'))
        },
        {
            '$set': {'hijos': hijo}
        }
    )


#Ejercicio 12: Para introducir una marca de coche en cada usuario
result=users.find({})
modelo=["Audi","Citroen","BMW","Ford","Volvo"]
for item in result:
    coche = modelo[randint(0, (len(modelo) - 1))]
    users.find_one_and_update(
        {
            '_id': ObjectId(item.get('_id'))
        },
        {
            '$set': {'coche':coche}
        }
    )
#Para eliminar a Maria
#result = users.remove({'email':"maria@mail.com"})
#pprint(result)



#Mofificamos los datos de Donal para que nos devuelva en el main la búsqueda que nos pide
result=users.find_one_and_update(
    {'nombre': "Donal"},
    {'$set':{'salario':45000}},
    return_document=ReturnDocument.AFTER)
print(result)


result=users.find_one_and_update(
    {'nombre': "María"},
    {'$set':{'status':False}},
    return_document=ReturnDocument.AFTER)
print(result)

result=users.find_one_and_update(
    {'nombre': "María"},
    {'$set':{'hijos':0}},
    return_document=ReturnDocument.AFTER)
print(result)

result=users.find_one_and_update(
    {'nombre': "Donal"},
    {'$set':{'coche':"Audi"}},
    return_document=ReturnDocument.AFTER)
print(result)