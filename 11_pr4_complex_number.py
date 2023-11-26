a=int(input("Enter the first complex number's real part:-"))
b=int(input("Enter the first complex number's imaginary part:-"))
d=int(input("Enter the second complex number's real part:-"))
e=int(input("Enter the second complex number's imaginary part:-"))

class Complex:
    def __init__(self , r , i):
        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return Complex(self.real+c.real , self.imaginary+c.imaginary)

    def __mul__(self,c):
        return Complex((self.real*c.real)-(self.imaginary*c.imaginary) , (self.real*c.imaginary)+(self.imaginary*c.real))

    def __str__(self):
        if(self.imaginary < 0):
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"

c1=Complex(a,b)
c2=Complex(d,e)
print("The sum of given two comlex numbers is:-",c1 + c2)
print("The multiplication of given two numbers is:-",c1*c2)