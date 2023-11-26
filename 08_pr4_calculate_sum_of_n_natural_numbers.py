a=int(input("Enter the number:-"))

def subition(n):
    if n<=1:
        return n
    else:
       return n + subition(n-1)

S=subition(a)
print("The sum of a natural number is ",S)