def insercion(list):
    for i in range(1, len(list)):
        x = list[i] #elemento a comparar
        j = i - 1    
        while j >= 0 and x < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = x
    return list

lista = [10,2,8,1,0]

print(insercion(lista))