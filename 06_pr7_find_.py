post=input("Enter the text:-")
spam=False

if("Karan" in post):
    spam=True
elif("KARAN" in post):
    spam=True
elif("K@R@N" in post):
    spam=True
elif("K@r@n" in post):
    spam=True
elif("karan" in post):
    spam=True
elif("KaRaN" in post):
    spam=True
elif("#Karan" in post):
    spam=True
else:
    spam=False 

if(spam):
    print("You are taking about karan.") 
else:
    print("You are not taking about karan.")