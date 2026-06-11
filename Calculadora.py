print("---- Calculadora SUPER basica ----")
numero1 = int(input("Escoge un numero "))
numero2 = int(input("Escoge un segundo numero"))

print("Suma = ", numero1+numero2)
print("Resta =", numero1-numero2)
print("Multiplicacion =", numero1*numero2)

if numero1 == 0 and numero2 == 0 :
    print("No se puede dividir 0 entre 0, no me arruines el codigo")
else:
    print("Division = ", numero1/numero2)


