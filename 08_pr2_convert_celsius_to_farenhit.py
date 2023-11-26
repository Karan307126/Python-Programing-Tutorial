C=float(input("Enter the calsius:-"))

def converter(calsius):
    farenhet=(calsius*(9/5))+32
    return farenhet

F=converter(C)
print("The farenhet tempreture is ",F)