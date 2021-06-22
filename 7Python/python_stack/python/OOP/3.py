def varargs(arg1, *args):#con * (operador splat) le indico que pueden venir argumentos variables
    print("Got ", arg1, " and ", args)

varargs("one") 			# salida: Got one and ()
varargs("one", "two") 	        # salida: Got one and ('two',)
varargs("one", "two", "three")  # salida: Got one and ('two', 'three')
#con operador splat se genera una tupla, por lo cual, se puede iterar como tal