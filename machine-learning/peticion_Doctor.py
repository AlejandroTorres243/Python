import urllib.request
import json
import csv

#DATOS
#ip = "10.63.176.134"
listado_ip = {"10.40.20.71","10.40.20.60","10.40.20.72","10.40.20.73","10.40.20.74"}
listado_id = {"21"}
#listado_id = {"33"} #38
#listado_id = {"30"}

'''
fecha_inicio = "2019-12-14" #aaaa-mm-dd
hora_incio = "00:00:00"     #00:00:00
fecha_fin = "2019-12-15"    #aaaa-mm-dd
hora_fin = "00:00:00"       #00:00:00
'''
fecha_inicio = "2019-12-14" #aaaa-mm-dd
hora_incio = "00:00:00"     #00:00:00
fecha_fin = "2019-12-15"    #aaaa-mm-dd
hora_fin = "22:59:59"       #00:00:00

#listado_variables = {"ULF_relevanttime_Q2_OFFSET_1"}
#listado_variables = {"mainpumpspre_2","bc1pre_1","slideringsecpre_1","slidepos_1","slidecentralsecpre_2","activepower_1","slideforce_1","hydfunc1retpre_1"}
listado_variables = {"clock_1","slideforce_1","slideforce_2","pump3pre_2","bc1force_1"}



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
