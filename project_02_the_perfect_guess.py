import random
randNumber=random.randint(1 , 100)
# print(randNumber)
userGuess=None
guesses=0
name = input("Enter your name : ")

while (userGuess != randNumber):
    userGuess=int(input("Enter the your guess:-"))
    guesses+=1
    if (userGuess==randNumber):
        print("Your guessed it right!")
    else:
        if (userGuess>randNumber):
            print("You guesseed it wrong! Enter a smaller number.")
        else:
            print("You guessed it wrong! Enteer a larger number.")
    
print(f"You guessed the number in {guesses} guesses.")

with open("Score.txt","a") as f:
    f.write(f"\n{name} score is : {guesses}")

with open("hiscore.txt","r") as f:
    hiscore = int(f.read())

if(guesses < hiscore):
    with open("hiscore.txt", "w") as f:
        print("You have just broken hiscore!")
        f.write(f"{guesses}")