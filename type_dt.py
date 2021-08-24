def type_dt(data):
   dt = str(type(data))
   if 'str' in dt:
      print('String')
   elif 'int' in dt:
      print('Integer')
   elif 'float' in dt:
      print('floating point number')
   elif 'complex' in dt:
      print('complex number')

type_dt(23)