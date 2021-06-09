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