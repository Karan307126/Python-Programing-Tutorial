list1=[3,53,2,False,9.53,"Karan"]

index = 0
for item in list1:
    print(f"{index} :- {item}")
    index += 1
print("\n")
for index, item in enumerate(list1):
    print(f"{index} :- {item}")