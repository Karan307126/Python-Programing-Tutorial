while(True):
    print("Press q or Q to quit.")
    a=input("Enter the number:-")
    if a=='q' or a=='Q':
        break
    try:
        print("Trying.........")
        a=int(a)
        if a>6:
            print("You entered a number greter than 6.")
    except Exception as e:
        print(f"Your input result in an error {e}.")

print("Thanks for playing this game.")