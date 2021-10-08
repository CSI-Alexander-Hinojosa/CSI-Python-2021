import random
print("Welcome to the rock, paper, scisors machine")
RPS= ["rock", "paper", "scissors"]

playerselection=input("Time to play, choose between rock, paper, or scissors\n")

computerChoice=random.choice(RPS)
print(f"Computer selected:{computerChoice}")
print(f"Player selected:{playerselection}")

if(playerselection==computerChoice):
    print("you tied, better luck next time")

elif(playerselection=="rock" and computerChoice=="scissors"):
    print("You win this time :/")
elif(playerselection=="rock" and computerChoice=="paper"):
    print("I win this time, as expected :) ")

elif(playerselection=="paper" and computerChoice=="rock"):
    print("You win this time :/")
elif(playerselection=="paper" and computerChoice=="scissors"):
    print("I win this time, as expected :)")

elif(playerselection=="scissors" and computerChoice=="paper"):
    print("You win this time :/")
elif(playerselection=="scissors" and computerChoice=="rock"):
    print("I win this time, as expected :)")

else:
    print("Something went wrong, check your answer.")