import urllib.request
import json
import csv

#DATOS
#ip = "10.63.176.134"
ip = "10.63.176.121"
id = "45"
fecha_inicio = "2019-02-13" #aaaa-mm-dd
hora_incio = "10:45:02"     #00:00:00
fecha_fin = "2019-02-13"    #aaaa-mm-dd
hora_fin = "10:45:30"       #00:00:00
listado_variables = {
"bc1force_1",
"bc1force_2",
"bc1servopilotpre_1",
"bc1servopilotpre_2",
"bc1accumoilpre_1",
"bc1accumoilpre_2",
"bc1stage_1",
"bc1stage_2",
"pump1pre_1",
"pump1pre_2",
"pump2pre_1",
"pump2pre_2",
"pump3pre_1",
"pump3pre_2",
"auxpumppre_1",
"auxpumppre_2",
"reducedauxpumppre_1",
"reducedauxpumppre_2",
"setvalueY40_1",
"setvalueY40_2",
"setvalueY41_1",
"setvalueY41_2",
"setvalueY42_1",
"setvalueY42_2",
"slidestage_1",
"slidestage_2",
"slideforce_1",
"slideforce_2",
"slidevel_1",
"slidevel_2",
"slidepos_1",
"slidepos_2",
"slidecentralsecpre_1",
"slidecentralsecpre_2",
"slidelateralsecpre_1",
"slidelateralsecpre_2",
"slideservopilotpre_1",
"slideservopilotpre_2",
"slideservicepre_1",
"slideservicepre_2",
"slidepfillmainpre_1",
"slidepfillmainpre_2",
"slidepfillcentralpre_1",
"slidepfillcentralpre_2",
"slidepfilllateralpre_1",
"slidepfilllateralpre_2",
"slidepfillunlockingpre_1",
"slidepfillunlockingpre_2",
"clock_1",
"clock_2"}

for variable in listado_variables:
    try:
        url_datos = "http://"+ip+"/oData/TagHistory?$filter=%20IdIndStudio%20eq%20%27"+id+"%27%20and%20(Name%20eq%20%27"+variable+"%27)%20and%20Timestamp%20gt%20"+fecha_inicio+"T"+hora_incio+".000Z%20and%20Timestamp%20lt%20"+fecha_fin+"T"+hora_fin+".000Z"

        print ("Extrayendo datos de " +variable)

        datos = urllib.request.urlopen(url_datos).read()

        my_json = datos.decode('utf8').replace("'", '"')
        data = json.loads(my_json)

        #print (data['value'][1]['Value'])

        file = open(str(variable)+'.csv', 'a', newline='')
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
