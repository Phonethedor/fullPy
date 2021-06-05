#imprimir
print ("test")
#variables
variable = 'ok'
print(variable)
print(variable+' concatenado')
#no se requiere declarar tipo de dato
numero = 10
#print(variable+numero)
#no se puede concatenar dos elementos distintos por lo que
#en el caso de arriba, hay que hacer parse al numero
print(variable,numero)
#tambien existe esta posibilidad
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"mi nombre es {first_name} {last_name} y tengo {age} años")
#asi es posible concatenar elementos dentro del string
print("Mi nombre es {} {} y tengo {} años.".format(first_name, last_name, age))
print("Mi nombre es {} {} y tengo {} años.".format(age, first_name, last_name))
#tambien es posible hacerlo de esa forma
hw = "Hola %s" % "mundo" 	# con valores literales
py = "Me encanta Python %d" % 3 
print(hw, py)
#forma antigua de concatenar, %s concatena string, %d concatena numeros
name = "Zen"
age = 27
print("Mi nombre es %s y tengo %d años" % (name, age))
#la misma forma que la anterior pero con distinto formato

#string.upper(): devuelve una copia de la cadena con todos los caracteres en mayúscula.

#string.lower(): devuelve una copia de la cadena con todos los caracteres en minúsculas.

#string.count(substring): devuelve el número de ocurrencias de subcadena en la cadena.

#string.split(char): devuelve una lista de valores donde la cadena se divide en el carácter dado. 
#Sin un parámetro, la división predeterminada está en cada espacio

#string.find(substring): devuelve el índice del inicio de la primera aparición de subcadena dentro de la cadena.

#string.isalnum(): devuelve booleano dependiendo de si la longitud de la cadena es> 0 y todos los caracteres 
#son alfanuméricos (solo letras y números). Las cadenas que incluyen espacios y signos de puntuación devolverán 
#False para este método. Métodos similares incluyen .isalpha(), .isdigit(), .islower(), .isupper(), 
#y así sucesivamente. Todos regresan booleanos.

#string.join(list):  devuelve una cadena que es todas las cadenas dentro de nuestro conjunto 
#(en este caso, una lista) concatenadas.

#string.endswith(substring): devuelve un valor booleano en función de si los últimos caracteres 
#de la cadena coinciden con la subcadena.

#string.replace('lo que se reemplazara','lo que quedara')
texto = 'Hola Mundo'
resultado = texto[2:8]
print(resultado)
#imprime los indices del array en cuestion
