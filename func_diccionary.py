# Hint : Use dictionary

guest_1 = 'jake'

guest_2 = 'tamra'

guest_3 = 'Ted'


dict_guests = {'Name':{'Jhon', 'Kyle', 'Tamra', 'Josh'}, 'Key':{'A011','A009', 'BQ02', 'A015', 'BQ13'}}


def get_key(guest,key):
    
	if(key != None):

	        dict_guests['Name'].add(guest)
        
        dict_guests['Key'].add(key)
 
        	print('Register')

	else:

   	     print('Not Registered')



get_key(guest_1, 'BQ02')

get_key(guest_2, 'A015')

get_key(guest_3, 'BQ13')

get_key('Luis', None)


print(dict_guests)