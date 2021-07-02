def agregarSueldos():
    sueldos = []
    for i in range(5):
        moneda = int(input("Ingrese su sueldo : "))
        sueldos.append(moneda)
    return sueldos

def impSueldos(sueldos):
    for i in range (len(sueldos)):
        print(sueldos[i])

def contarSueldos(sueldos):
    c = 0
    for i in range (len(sueldos)):
        if sueldos[i] > 1000:
            c +=1
    return c

def promSueldos(sueldos):
    sum = 0
    for i in range (len(sueldos)):
        sum += sueldos[i]
    return sum/len(sueldos)

def menorProm(sueldos):
    prom = promSueldos(sueldos)
    for i in range (len(sueldos)):
        if sueldos[i] < prom:
            print(sueldos[i])

sueldo1 = agregarSueldos()
impSueldos(sueldo1)
print(contarSueldos(sueldo1))
print(promSueldos(sueldo1))
menorProm(sueldo1)