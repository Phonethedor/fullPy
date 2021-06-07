import random

def randint(min=0   ,max=0):
    if (min == 0 and max == 0):
        return random.randint(0,100)
    elif (min==0 and max!=0 and max > 0):
        return random.randint(0,max)
    elif (min==0 and max!=0 and max < 0):
        return "el numero maximo ingresado es menor a 0"
    elif (min!=0 and max==0 and min < 100):
        return random.randint(min,100)
    elif (min!=0 and max==0 and min < 100):
        return "el numero minimo ingresado es mayor a 100"
    else:
        return random.randint(min,max)