#datos
#para crear bloques de codigo la sangria es lo mas importante
#ya que indica que se encuentran dentro del bloque
x = 10
if x > 50:
    print("ok")
else:
    print("no")
#claro ejemplo de bloque condicional

class EmptyClass:
    pass
#de esta manera declaramos el fragmento de codigo sin error, ya que posee la funcion pass

#tuplas son como los array pero una ves definidos, son INCAMBIABLES
dog = ('Bruce', 'cocker', 19, False)

#listas son literal array
lista = [1,'2',True]
#para obtener datos de tanto las tuplas como las listas, se usa el apendice al igual que en los array

#funciones en listas
lista.pop()
lista.pop(0)
#si pop no posee el indice, procede a eliminar el ultimo elemento, si lo posee borra el elemento en cuestion
lista.append('añade al final')

#diccionarios
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
#grupo de pares clave-valor sus valores pueden cambiar de la siguiente forma
new_person ['name'] = 'Jack'
new_person['hobbies'] = ['climbing', 'coding']	# agrega un par clave-valor si la clave no existe
print (new_person)
print(new_person['name']) #asi se extrae el valor correspondiente

print(type(new_person)) #devuelve el tipo de dato

print(len(new_person))#devuelve el valor de lenght

print("Hello" + str(42)) #asi se pueden unir datos

total = 35
user_val = "26"
total = total + user_val
total = total + int(user_val)		# total será 61
#se puede ya que transforma el texto a int
