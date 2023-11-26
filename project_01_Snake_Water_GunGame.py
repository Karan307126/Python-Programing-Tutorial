import random

def gamewin(comp,you):
   if comp==you:
       return None
   elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
   elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
   elif comp=='g':
        if you=='w':
            return True
        elif you=='s':
            return False



your_score=0 
Computer_score=0
for i in range(3):
    you=input("Your Turn:Snake(s) Water(w) or Gun(g)?:-")
    print(f"You chose:-->{you}")
    print("............................................")

    print("Comp Turn:Snake(s) Water(w) or Gun(g)?")
    randNo=random.randint(1,3)
    if randNo==1:
        comp='s'
    elif randNo==2:
        comp='w'
    elif randNo==3:
        comp='g'

    print(f"Computer chose:-->{comp}")
    print(".............................................")

    a=gamewin(comp,you)
    if a==None:
        print("The match is a tie!")
        your_score=your_score + 1
        Computer_score=Computer_score + 1
    elif a:
        print("You win the match!")
        your_score=your_score + 1
    else:
        print("You lose the match!")
        Computer_score=Computer_score + 1
    print("..............................................")
    
    print("Your score is:-",your_score)
    print("Computer score is:-",Computer_score)
    print("______________________________________________")
    print("______________________________________________")
if your_score>Computer_score:
    print("***** Final Result *****")
    print("You win the match!")
    print("Computer lose the match!")
elif your_score<Computer_score:
    print("***** Final Result *****")
    print("You lose the match!")
    print("Computer win the match!")
elif your_score==Computer_score:
    print("***** Final Result *****")
    print("The match is tie!")