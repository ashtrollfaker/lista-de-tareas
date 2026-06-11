print("----- Generador de contraseñas -----")
import random
random.randint(0, 1000)
longitud = int(input("¿Cuantos caracteres quieres que tenga tu contraseña? "))
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=,./<>?;:[]{}|"
contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)
print("Tu contraseña es: " + contraseña)

