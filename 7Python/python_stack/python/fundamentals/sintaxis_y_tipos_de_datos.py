x =70 #variable
if x > 50:
    print("mayor que 50")
    pass
else:
    pass
    print("menor que 50")

# tipos de datos primitivos
# booleanos --> true y false
# numeros enteros --> alamcena un int y numeros de coma flotante --> almacena un float
age = 35
if age > 30:
    print("Verdadero")
    pass
else:
    pass
    print("Falso")

# tipos compuestos

# tuplas --> tipo de datos inmutable, pueden contener datos mixtos

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# salida: Bruce
# dog[1] = 'dachshund'	# ERROR: no se puede modificar (el objeto 'tupla' no admite la asignación de elementos)

# listas

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# salida: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# salida: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# salida: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# salida: ['Francis', 'Oliver']

# diccionarios

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# actualiza si la llave existe
new_person['hobbies'] = ['climbing', 'coding']	# agrega un par clave-valor si la clave no existe
print(new_person)	
# salida: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# remueve la clave especifica y retorna el valor
print(w)		# salida: 160.2
print(new_person)	
# salida: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}    

# funciones comunes

#type

print(type(2.63))		# salida: <class 'float'>
print(type(new_person))		# salida: <class 'dict'>

# len (longitud)

print(len(new_person))		# salida: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# salida: 11

# Conversion de tipo o conversion de tipo explicito

# print("Hello" + 42)			# salida: TypeError
print("Hello" + str(42))		# salida: Hello 42

total = 35
user_val = "26"
total = total + int(user_val)		# total será 61
print(total)