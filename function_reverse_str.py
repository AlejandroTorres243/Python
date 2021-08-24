Str1 = 'Desserts'

Str2 = "Live" 

Str3 = 'Pals'

Str4 = 'God'

Str5 = 'Raw'

def str_rev(stra):

    palabra = ''

    for letter in stra:

	    palabra = letter + palabra

     print('' + stra + ':' palabra)

str_rev(Str1)