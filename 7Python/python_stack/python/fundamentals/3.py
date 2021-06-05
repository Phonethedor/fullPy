#operadores logicos y bucles
x =  12 
if x >  50 :
    print( "mayor que 50" )
else :
    print( "menor que 50" )
# porque x no es mayor que 50, la segunda instrucción de impresión es la única que se ejecutará
    
x =  55 
if x >  10 :
    print( "mayor que 10" )
elif x >  50 :
    print( "mayor que 50" )
else :
    print( "menor que 10" )
# aunque x sea mayor que 10 y 50, la primera declaración verdadera es la única que se ejecutará, por lo que solo veremos 'mayor que 10'
    
if x <  10 :
    print( "menor que 10" )
# no sucede nada, porque la declaración es falsa

#para and, or y not, es la palabra literal

#ciclo for
#for x in range(0, 10, 1):
#for x in range(0, 10):	 incremento de +1 está implícito
#for x in range(10):	 incremento de +1 e inicia en 0 está inplicito
for x in range(0, 10, 2):
    print(x)
# salida: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# salida: 5, 2

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# salida: 0 abc, 1 123, 2 xyz

for v in my_list:
    print(v)
# salida: abc, 123, xyz

#ciclo while
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final de sentencia else")

#break, al agregar break a un ciclo, se le indica que si se cumple el codigo, se debe salir del ciclo
for val in "string":
    if val == "i":
        break
    print(val)
# salida: s, t, r

#continue, si la condicion se cumple, vuelve al ciclo de inmediato
for val in "string":
    if val == "i":
        continue
    print(val)
# salida: s, t, r, n, g
