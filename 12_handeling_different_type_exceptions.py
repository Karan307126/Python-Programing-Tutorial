try:
    a=int(input("Enter the number:-"))
    c=1/a
    print(c)
except ValueError as e:
    print("Exeption1 qccured:")
    print(e)

except ZeroDivisionError as e:
    print("Exeption2 occured:")
    print(e)

print("Thanks for using this code!")
