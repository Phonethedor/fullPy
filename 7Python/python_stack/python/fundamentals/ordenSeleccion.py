def ordenSeleccion(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list

lista = [10,2,8,1,0]

print(ordenSeleccion(lista))