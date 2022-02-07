import random
word_list = ["Brasília","BuenosAires", "Lima", "Asunción", "SanSalvador", "Sucre", "Bogota", "Caracas", "Quito", "SanJosé"]

# Cual es la capital de Brazil- Brasília
# Cual es la capital de Agentina- Buenos Aires 
# Cual es la capital de Perú- Lima 
# Cual es la capital de Paraguay- Asunción
# Cual es la capital de El Salvador- San Salvador

# Cual es la capital de Bolivia- Sucre
# Cual es la capital de Colombia- Bogota
# Cual es la capital de Venezuela- Caracas 
# Cual es la capital de Equador- Quito 
# Cual es la capital de Costa Rica- San José

def get_word (word_list):
    word = random.choice (word_list)
    return word.upper()

# .upper()-para colocar una palabra en mayuscula.


def play (word):
    word_completion= "-" * len (word)
    guessed= False
    guessed_letters =[]
    guessed_words =[]
    tries=6 
    print("Hola, jueguemos a colgado")
    print("Tema: Capitales de LatinoAmerica.")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess=input("Adivina una letra o palabra ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("Ya usastes", guess,"!")
            elif guess not in word:
                print(guess,"No esta en la palabra :(")
                tries -= 1
                guessed_letters.append (guess)
            else:
                print("Bien hecho", guess, "esta en la palabra!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices= [i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completion= "".join (word_as_list)
                if "-" not in word_completion:
                    guess=True 
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Ya usastes", guess,"!")
            elif guess != word:
                print(guess,"No esta en la palabra :(")
                tries-=1
                guessed_words.append (guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Input inválido")
        print(display_hangman(tries))
        print(word_completion)
        print("\n") 

    if guessed:
        print("Enhorabuena, has acertado la palabra :)")
    else:
        print("Lo siento, pero se te han acabado las vidas. :( La palabra era" + word + "Mejor suerte la próxima")



def display_hangman (tries):
    stages = [  """
                        ____________________
                        |                  I
                        |                  I
                        O                  I
                       /|\\                I
                        |                  I
                       / \\                I
                                           I
                                           I
--------------------------------------------
                        """,
                        """
                        ____________________
                        |                  I
                        |                  I
                        O                  I
                       /|\\                I
                        |                  I
                       /                   I
                                           I
                                           I
--------------------------------------------
                        """,
                        """
                        ____________________
                        |                  I
                        |                  I
                        O                  I
                       /|\\                I
                        |                  I
                                           I
                                           I
                                           I
--------------------------------------------
                        """,
                        """
                        ____________________
                        |                  I
                        |                  I
                        O                  I
                       /|                  I
                        |                  I
                                           I
                                           I
                                           I
--------------------------------------------
                        """,
                        """
                        ____________________
                        |                  I
                        |                  I
                        O                  I
                        |                  I
                        |                  I
                                           I
                                           I
                                           I
--------------------------------------------
                        """,
                        """
                        ____________________
                        |                  I
                        |                  I
                        O                  I
                                           I
                                           I
                                           I
                                           I
                                           I
--------------------------------------------
                        """,
                        """
                        ____________________
                        |                  I
                        |                  I
                                           I
                                           I
                                           I
                                           I
                                           I
                                           I
--------------------------------------------
                        """
    ]
    return stages [tries]

def main():
    word = get_word (word_list)
    play(word)
    while input("Quieres jugar de nuevo? (Y/N)").upper() == "Y":
        word = get_word (word_list)
        play(word)

if __name__== "__main__":
    main()

