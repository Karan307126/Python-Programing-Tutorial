a = int(input("Enter the value : "))
b = int(input("Enter the value : "))


try:
    print(a / b)
    k = int(input("Enter number : "))
    print(k)

except ZeroDivisionError:
    print("Hey, You can't devide by zero any number.")

except ValueError:
    print("Invalid input you have entered.")

except Exception as e:
    print("Something went wrong...")
    print(e)
    
finally:
    print("*****    Thanks for using my code.   *****")