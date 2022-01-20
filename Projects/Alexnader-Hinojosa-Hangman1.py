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
--------------------------------------------]