#GAME 1
# Number guessing game
import random

number = random.randint(1, 49)
guess = None

while guess != number:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        elif guess == number:
            print(f"Gotch! The number is {number}")
    except ValueError:
        print("  -> Error! Enter a valid integer input")
      
#GAME 2
# Rock, paper, Scissors game    
import random

choices = ["r", "p", "s"]
computer = random.choice(choices)
player = input("Choose rock(r), paper(p), or scissors(s): ")
print(f"Computer: {computer} | Player: {player}")

if player == computer:
    print("It's a tie!")
elif (player == "r" and computer == "s") or (player == "p" and computer == "r") or (player == "s" and computer == "p"):
    print("You win!")
else:
    print("Computer wins!")
