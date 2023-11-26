marks=int(input("Enter your marks:-"))

if(90<=marks<=100):
    print("Your gread is Ex..")
elif(80<=marks<90):
    print("Your gread is A.")    
elif(70<=marks<80):
    print("Your gread is B.")    
elif(60<=marks<70):
    print("Your gread is C.")    
elif(50<=marks<60):
    print("Your gread is D.")
else:
    print("Your gread is F.")        


# Another trick to solve problem
if marks>=90:
    gread="Ex."
elif marks>=80:
    gread="A"
elif marks>=70:
    gread="B"
elif marks>=60:
    gread="C"
elif marks>=50:
    gread="D"
else:
    gread="F"    

print("Yourgread is "+gread)    