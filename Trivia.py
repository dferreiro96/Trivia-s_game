"""
juego de trivia:crea un diccionario con preguntas y respuestas.
pregunta al usuario y lleva la puntuación.
<< >> \n
Creas un diccionario con preguntas y respuestas.
El programa muestra una pregunta.
El usuario responde.
El programa dice si acertó o no.
Al final, muestra la puntuación total.
"""
import random
print("Juego de trivia:crea un diccionario con preguntas y respuestas. \nPregunta al usuario y lleva la puntuación.")
jugar= True
while jugar:
    
    preguntas = {
    "¿Cuál es la capital de Francia?": "París",
    "¿Cuánto es 7 x 8?": "56",
    "¿Quién escribió 'Cien años de soledad'?": "Gabriel García Márquez",
    "¿Cuál es el planeta más grande del sistema solar?": "Júpiter",
    "¿En qué año llegó el hombre a la Luna?": "1969",
    "¿Cuál es el océano más grande del mundo?": "Pacífico",
    "¿Cuántos continentes hay en el mundo?": "7",
    "¿Cuál es el símbolo químico del oro?": "Au",
    "¿Quién pintó la Mona Lisa?": "Leonardo da Vinci",
    "¿Cuál es el río más largo del mundo?": "Amazonas"
    }
    
    acierto=0
    contador=0

    pregunta= (list(preguntas))
    random.shuffle(pregunta)
    
    for i, clave in enumerate(pregunta, start=1):
        contador+=1
        respuesta= input(f"\nPregunta número {i} o presione 's' para 'salir': {clave}: ").lower() .strip() 
        if respuesta in ("s", "SALIR", "salir"):
            print("\nHasta luego")
            jugar= False
            break
            
        if respuesta== preguntas[clave].lower() .strip():
            print("Acertó. FELICIDADES !!")
            acierto+=1
        else:
            print("Respuesta incorrecta")
            
    while jugar:     
        print(f"Acertó un total de {acierto} preguntas.")
        
        while True:
            jugar_otra_vez= input("Desea jugar otra vez? (s/n): ") .lower() .strip()
            if jugar_otra_vez in ("si", "sí", "SI", "SÍ"):
                print()
                break
            elif jugar_otra_vez in ("no", "NO","n"):
                print("\nHasta luego")
                print(f"Jugó {contador} veces.")
                jugar= False
            else:
                print("Caracter inválido")
            

            