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

