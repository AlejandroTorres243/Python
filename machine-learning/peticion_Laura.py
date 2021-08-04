import urllib.request
import json
import csv

#DATOS
#ip = "10.63.176.134"
listado_ip = {"10.63.176.121","10.63.176.134","10.63.176.67","10.63.176.187","10.63.177.10"}
listado_id = {"14","15","16","13","12","17","18","19","20","21","22","23","24","25","26","27",
"28","29","30","31","32","33","34","35","36","39","40","41","42","43","44","45","47","48"}
fecha_inicio = "2018-03-27" #aaaa-mm-dd
hora_incio = "00:00:01"     #00:00:00
fecha_fin = "2019-03-27"    #aaaa-mm-dd
hora_fin = "23:59:59"       #00:00:00
listado_variables = {
"Alarm_Wm_G01_02_1",
"Alarm_Wm_G01_02_2",
"Alarm_Fi_G01_00_1",
"Alarm_Fi_G01_00_2"}



for ip in listado_ip:
    for id in listado_id:
        for variable in listado_variables:
            try:

                #url_datos = "http://"+ip+"/oData/TagHistory?$filter=IdIndStudio eq '"+id+"' and (Name eq '"+variable+"') and Timestamp gt "+fecha_inicio+"T"+hora_incio+".000Z and Timestamp lt "+fecha_fin+"T"+hora_fin+".000Z"
                url_datos = "http://"+ip+"/oData/TagHistory?$filter=%20IdIndStudio%20eq%20%27"+id+"%27%20and%20(Name%20eq%20%27"+variable+"%27)%20and%20Timestamp%20gt%20"+fecha_inicio+"T"+hora_incio+".000Z%20and%20Timestamp%20lt%20"+fecha_fin+"T"+hora_fin+".000Z"

                print ("Extrayendo datos de " +variable+ " " + ip + " " + id)

                datos = urllib.request.urlopen(url_datos).read()

                my_json = datos.decode('utf8').replace("'", '"')
                data = json.loads(my_json)

                file = open("id-"+str(id)+" tag-"+str(variable)+'.csv', 'a', newline='')
                # create the csv writer object
                csvwriter = csv.writer(file)

                count = 0
                for emp in data['value']:
                    if count == 0:
                        header = emp.keys()
                        csvwriter.writerow(header)
                        count += 1
                    csvwriter.writerow(emp.values())
                file.close()

            except:
                print ("error al acceder a la variable " + str(variable))
