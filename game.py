import random
# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
"inteligencia"]
# Elegir una palabra al azar
secret_word = random.choice(words)
# Número máximo de intentos permitidos
max_failures = 3
attemps = 0
# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
difficulty = str(input("Elija una de las siguientes dificultades: \"facil\" - \"media\" - \"dificil\" "))
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = ""
if (difficulty == "facil"):
    for i in secret_word:
        match i:
            case "a":
                word_displayed += "a"
                guessed_letters += "a"
            case "á":
                word_displayed += "á"
                guessed_letters += "á"
            case "e":
                word_displayed += "e"
                guessed_letters += "e"
            case "é":
                word_displayed += "é"
                guessed_letters += "é"
            case "i":
                word_displayed += "i"
                guessed_letters += "i"
            case "í":
                word_displayed += "í"
                guessed_letters += "í"
            case "o":
                word_displayed += "o"
                guessed_letters += "o"
            case "ó":
                word_displayed += "ó"
                guessed_letters += "ó"
            case "u":
                word_displayed += "u"
                guessed_letters += "u"
            case "ú":
                word_displayed += "ú"
                guessed_letters += "ú"
            case _:
                word_displayed += "_"
elif (difficulty == "media"):
    word_displayed += secret_word[0]
    for i in range (1,(len(secret_word)-1)):
        word_displayed += "_"
    word_displayed += secret_word[-1]
else:
    word_displayed = "_" * len(secret_word)
# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")
while (attemps <= max_failures):
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)  
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word and letter != "":
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        attemps += 1
        # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    if (difficulty == "media"):
        letters.pop(0)
        letters.pop()
        letters.insert(0,secret_word[0])
        letters.append(secret_word[-1])
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    #Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_failures} fallos posibles.")
    print(f"La palabra secreta era: {secret_word}")