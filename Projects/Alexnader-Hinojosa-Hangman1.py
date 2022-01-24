import random

word_list = ["Brazilia","Buenos Aires", "Lima", "Asunción", "San Salvador", "Sucre", "Bogota", "Caracas", "Quito", "San José"]

# Cual es la capital de Brazil- Brazilia
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
    word= random(word_list)
    return word.upper()

# .upper()-para colocar una palabra en mayuscula.


def play(word):
    word_completion= "_" * len (word)
    guessed=False
    guessed_letters = []
    guessed_words=[]
    tries=6 
    print("Hola, jueguemos a colgado")
    print("Tema: Bienvenidos a LatinoAmerica.")
    print(display_Hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess=input("Adivina una letra o palabra ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("Ya usastes", guess,"!")
            elif guess not in word:
                print(guess,"No esta en la palabra :(")
                tries-=1
                guessed_letters.append(guess)
            else:
                ("Bien hecho", guess, "esta en la palabra!")
                guessed_letters.append(guess)





def display_Hangman(tries):
    stages= ["""
                        ____________________
                        |                  I
                        |                  I
                        O                  I
                       /|\                 I
                        |                  I
                       / \                 I
                                           I
                                           I
--------------------------------------------
""",

"""
                        ____________________
                        |                  I
                        |                  I
                        O                  I
                       /|\                 I
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
                       /|\                 I
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
"""]