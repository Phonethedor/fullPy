def operar(a,b,c):
    x = a+b*c
    return x

variable = operar(5,10,2)
print(variable)


def saludar(saludo):
    print("El saludo de hoy es: "+saludo)

saludar('Buenas Tardes!!')


''' Crear un función que solicite por pantalla el ingreso de 4 números enteros y los retorne'''
''' Crear una segunda función que reciba como parámetro la lista y que muestre todos los 
valores positivos'''

def crearLista():
    '''Definiendo la lista'''
    lista = []
    for var in range(4):
        variable = int(input("Ingrese el número: "))
        lista.append(variable)
    return lista

def mostrarPositivos(lista):
    print("Mostrando los valores positivos")
    for i in range(len(lista)):
        if lista[i]>0:
            print(lista[i])

listaNumeros = crearLista()

mostrarPositivos(listaNumeros)


'''' Crear una función que solicite el ingreso de 3 nombres junto con sus edades los cuales se
deben retornar'''
''' Crear una segunda función que permita recibir como parametros de nombre y edad para
imprimir los nombres de las personas mayores de 18 años'''
''' Crear una funcion que imprima el promedio de las edades'''

def pedirDatos():
    nombre = []
    edad = []
    for i in range(3):
        name = input("Ingrese su nombre: ")
        nombre.append(name)
        age = int(input("Igrese su edad: "))
        edad.append(age)
    return [nombre, edad]

def imprimirMayores(name, age):
    print("Las personas mayores de edad")
    for i in range(len(age)):
        if age[i]>=18:
            print(name[i])

def imprimirPromedio(edades):
    suma = 0
    for i in range(len(edades)):
        suma += edades[i]
    promedio = suma/3
    print("La edad promedio es: ", promedio)

nombres, edades = pedirDatos()
imprimirMayores(nombres, edades)
imprimirPromedio(edades)