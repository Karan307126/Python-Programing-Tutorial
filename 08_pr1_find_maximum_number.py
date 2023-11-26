a=int(input("Enter the number1:-"))
b=int(input("Enter the number2:-"))
c=int(input("Enter the number3:-"))


def max(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3

    else:
        if(num2>num3):
            return num2
        else:
            return num3

M=max(a,b,c)
print("The maximum number is ",M)