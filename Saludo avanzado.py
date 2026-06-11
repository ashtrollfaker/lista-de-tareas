print("----- Hola amigos del yutub -----")
nombre = input("¿Como te llamas? ")
edad = int(input("¿Cuantos años tienes? ")) 

if edad < 13:
    print("Lo siento, me dan miedo los menores de edad, asi que no puedo saludarte")
elif edad >= 13 and edad < 18:
    print("Eres un adolescente como yo (tengo 17 años), espero que te guste el contenido que vaya subiendo dia a dia")
elif edad > 18:
    print("Eres ya mayor de edad, espero que me contactes si llego a ser un experto en algo, porque me gustaria ayudar a los demas con lo que aprenda en un futuro")

