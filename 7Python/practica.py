#construir una funcion que pregunte por el ingreso de 2 valores
#esta funcion debe retornar los valores y entragar los numeros a otras funciones
#para calcular la suma, resta, multiplicacion y division (fucniones por separado)+
#agregue una funcion para imprimir todos los valores calculados

def calculadora():
    valor1 = int(input('ingrese el primer numero: '))
    valor2 = int(input('ingrese el segundo numero: '))
    suma = valor1 + valor2
    resta = valor1 - valor2
    mult = valor1 * valor2
    div = valor1 / valor2
    msg = 'El primer valor es '+str(valor1)+' el segundo valor es '+str(valor2)+' su suma es: '+str(suma)+' su resta es: '+str(resta)+' su multiplicacion es: '+str(mult)+' y su division es: '+str(div)
    return print(msg)

calculadora()

#ingrese por pantalla el numero de productos que desea comprar luego ingrese el precio de cada producto
#debe mostrar resultado de la compra del producto, agregando IVA al resultado final

def market():
    cantProducto = int(input('Ingrese la cantidad de productos que desea comprar : '))
    precioProducto = int(input('Ingrese el precio del producto : '))
    total = cantProducto+precioProducto
    msg = 'Ud compro '+str(cantProducto)+' cada uno con el siguiente valor '+str(precioProducto)+' el total mas IVA es: '+str(total+total*0.19)
    return print(msg)
market()

#utilice funciones para calcular lo siguiente:
#ingrese por pantalla 4 notas, calcule el promedio de presentacion a examen
#solicite la nota del examen, valide rango  de las notas entre 1 a 7
#el alumno debe obtener en el examen al menos un 3.5 para aprobar el curso
#el alumno aprueba con un promedio mayor o igual a 3.95
# imprima el promedio y el estado del alumno aprobado o reprobado
#calcule el promedio final de la nota de presentacion y la nota del examen
#nota de presentacion es un 70% y el examen es 30%

def notas():
    n1 = float(input('Ingrese la primera nota: '))
    if n1 <= 7 and n1 >= 1:
        n2 = float(input('Ingrese la segunda nota: '))
        if n2 <= 7 and n2 >= 1:
            n3 = float(input('Ingrese la tercera nota: '))
            if n3 <= 7 and n3 >= 1:
                n4 = float(input('Ingrese la cuarta nota: '))
                if n4 <= 7 and n4 >= 1:
                    total = n1+n2+n3+n4
                    prom = total/4
                    print('su promedio de notas para presentacion a examen es: '+str(prom))
                    if prom < 3.95:
                        return print('ud ha reprobado el curso, sin posibilidad de rendir examen')
                    else:
                        examen = float(input('Ingrese su nota de examen: '))
                        if examen <= 7 and examen >= 1:
                            nf = prom*0.7 + examen*0.3
                            print('Su nota final es: '+str(nf))
                            if nf < 3.95:
                                return print('ud ha reprobado el curso')
                            else:
                                return print('ud ha aprobado el curso, felicidades')
                        else:
                            return print('Nota inexistente')
                else:
                    return print('Nota inexistente')
            else:
                return print('Nota inexistente')
        else:
            return print('Nota inexistente')
    else:
        return print('Nota inexistente')

notas()