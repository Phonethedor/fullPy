def regresiva(num):
    regreso = []
    for num in range(num,-1,-1):
        regreso.append(num)
    print(regreso)

regresiva(5)

def print_and_return(list):
    print(list[0])
    return list[1]

print_and_return([4,2])

def fpl (list):
    return list[0]+len(list)

fpl ([1,2,3])

def mts (list):
    mayor = []
    if(len(list) == 0 or len(list) == 1):
        return False
    else:
        for x in range(0,len(list),1):
            if (list[x] > list[1] and list[x] != list[1]):
                mayor.append(list[x])
    print(len(mayor))
    return mayor

mts([1,2,3,4])

def lav (a,b):
    list = []
    for x in range(1,a+1):
        list.append(b)
    return list

a = lav (4,1)
print(a)