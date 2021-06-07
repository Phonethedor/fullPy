def biggie_size(list):
    lista = list
    for x in range(len(list)):
        if (list[x]<0):
            lista[x] = 'big'
    return lista

def count_positives(list):
    c = 0
    for x in range(len(list)):
        if (list[x]>0):
            c += 1
    list[len(list)-1] = c
    return list

def tsum (list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
    return sum

def prom (list):
    sum = 0
    for x in range(len(list)):
        sum += list[x]
    return sum/len(list)

def longitud (list):
    return len(list)

def minimum (list):
    if (len(list)!=0):
        min = list[0]
        for x in range (1,len(list)):
            if (list[x] < min):
                min = list[x]
    else:
        min = "ingrese una lista valida"
    return min

def maximum (list):
    if (len(list)!=0):
        max = list[0]
        for x in range (1,len(list)):
            if (list[x] > max):
                max = list[x]
    else:
        max = "ingrese una lista valida"
    return max

def uAnalisis (list):    
    if (len(list) != 0):
        msg = {}
        sum = 0
        min = list[0]
        max = list[0]
        for x in range (len(list)):
            sum += list[x]
            if (list[x]<min):
                min = list[x]
            if (list[x]>max):
                max = list[x]
        msg = {'suma total' : sum, 'numero mayor' : max, 'numero menor' : min, 'promedio' : sum/len(list)}
        return msg
    else:
        return 'ingrese una lista valida'

def revertir(list):
    if (len(list) != 0):
        list.reverse()
        return list
    else:
        return "ingrese una lista valida"