print("Abre la caja fuerte")

import random
numero_secreto = random.randint(1,20)

for i in range(1,8):
    numero = int(input("Escoge un numero "))


    if numero == numero_secreto:
        print("Accediendo")
        break
    else: 
       print("Acceso denegado")