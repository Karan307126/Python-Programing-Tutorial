sub1=int(input("Enter a marks sub1:-"))
sub2=int(input("Enter a marks sub2:-"))
sub3=int(input("Enter a marks sub3:-"))

avg=(sub1+sub2+sub3)/3

if(sub1>33 and sub2>33 and sub3>33 and avg>40):
    print("You are pass in all subjects.")
else:
    print("You are not pass in all subjects or fail in all subjects")    