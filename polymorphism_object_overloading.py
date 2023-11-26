class Number:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self,num):
        print("Let's add!")
        s1 = self.num1 + num.num1
        s2 = self.num2 + num.num2
        return s1, s2
    
    def __mul__(self,num):
        print("Let's multiply!")
        m1 = self.num1 * num.num1
        m2 = self.num2 * num.num2
        return m1, m2
   
    def __floordiv__(self,num):
        print("Let's divide!")
        d1 = self.num1 // num.num1
        d2 = self.num2 // num.num2
        return d1, d2

n1=Number(45, 65)
n2=Number(5, 13)
sum = n1 + n2
print(sum)
mul = n1 * n2
print(mul)
floordiv = n1 // n2
print(floordiv)