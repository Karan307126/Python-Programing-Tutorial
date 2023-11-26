a=int(input("Enter the number:-"))

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1)

f=factorial_recursive(a)
print(f)