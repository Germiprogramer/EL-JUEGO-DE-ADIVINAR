import random
numero = random.randint(0,100)
contador = 1

print("BIENVENIDO AL JUEGO DE ADIVINAR")

while numero < 100:
    intento = int (input ("Dime un numero del 1 al 99: "))
    if numero > intento:
        print("muy pequeña")
    elif numero < intento:
        print("demasiado grande")
    else:  
        print("FELICIDADES CAMPEÓN")
    if intento == numero:
        break
    contador += 1

if contador < 5:
    print ("Has usado ",contador, " intentos" )    
else:
    print("Has usado ",contador, " intentos, eres muy cojo")