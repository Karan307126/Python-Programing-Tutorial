I=float(input("Enter the Inches:-"))

def converter(Inches):
    cms=Inches/2.54
    return cms

C=converter(I)
print("The leanth in centimeter is ",C)