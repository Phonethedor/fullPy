#1
for x in range(1,151):
    print(x)

#2
for x in range (5,1001,5):
    print(x)

#3
for x in range (1,101):
    print(x)
    if(x % 5 == 0):
        print("Coding")
    if(x % 10 == 0):
        print("Dojo")

#4
suma = 0
for x in range (500000):
    if(x%2 != 0):
        suma += x

print(suma)

#5
for x in range(2018,-1,-4):
    print(x)

#6
for mult in range(1,6):
    for highNum in range(10,21):
        for lowNum in range(1,11):
            if (highNum%mult == 0 and lowNum%mult == 0):
                print(mult,lowNum,highNum)