def getOption(n):
    if n == 2:
        return "abc"
    elif n == 3:
        return "def"
    elif n == 4:
        return "ghi"
    elif n == 5:
        return "jkl"
    elif n == 6:
        return "mno"
    elif n == 7:
        return "pqrs"
    elif n == 8:
        return "tuv"
    else:
        return "wxyz"

def keypad(num):
    if num == 0:
        output = ""
        return output
    
    lastDigit = num % 10
    remainingDigit = num / 10

    smallOutput = keypad(remainingDigit)
    lastDigitOption = getOption(lastDigit)
    for i in range(0, smallOutput.__len__):
        for j in range(0, lastDigitOption.__len__):
            output = smallOutput + lastDigitOption
    
    return output


n = int(input("Enter number : "))

keypad(n)