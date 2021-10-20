import random

print("Welcome to the magic 8 ball temple")

Name=input("What is your name:")
print(f"Hello: {Name}")
playerselection=input("What do you want to ask me?\n")
random_number=random.randint(1,12)
print(f"{Name} asks: {playerselection}")

if random_number == 1:
    print("Yes-definitely")
elif random_number == 2:
    print("It is decidedly so")
elif random_number == 3:
    print("Without a doubt")
elif random_number == 4:
    print("Reply hazy, tracy, again")
elif random_number == 5:
    print("Ask again later")
elif random_number == 6:
    print("Better not tell you now")
elif random_number == 7:
    print("My sources say no")
elif random_number == 8:
    print("Outloock not so good")
elif random_number == 9:
    print("Very doubtful")
elif random_number == 10:
    print("Only time would tell")
elif random_number == 11:
    print("It is up to luck")
elif random_number == 12:
    print("soon you would know ")
else:
    print("Something went wrong, check your question.")
