import random
numero = random.randint(0,100)
contador = 1

print("BIENVENIDO AL JUEGO DE ADIVINAR")
intento = int (input ("Dime un numero del 1 al 99: "))
if intento < 0 or intento > 99:
    print("Limitate a seguir las normas")
    intento = int (input ("Dime un numero del 1 al 99: "))
while numero != intento:
    if numero > intento:
        print("muy pequeño")
        intento = int (input ("Dime un numero del 1 al 99: "))
    elif numero < intento:
        print("demasiado grande")
        intento = int (input ("Dime un numero del 1 al 99: "))

    if intento == numero:
        print("FELICIDADES CAMPEÓN")   
    
    contador += 1

if contador < 5:
    print ("Has usado ",contador, " intentos" )    
else:
    print("Has usado ",contador, " intentos, necesitas mejorar")