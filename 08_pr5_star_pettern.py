a=int(input("Enter the number:-"))

def pettern(number):
    for i in range(number):
        print("* "*(number-i))

pettern(a)