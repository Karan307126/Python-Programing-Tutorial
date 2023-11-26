myDict={
    "Pankha":"Fan",
    "Khurasi":"Chair",
    "Vastu":"Items",
    "Bandar":"Monkey"
}
print("Options are available is:-",myDict.keys())
a=input("Enter the Hindi world:-")
# print("The meaning of your word is:-",myDict[a])

# Below line will not throw an error if the key is not present in dictionary
print("The meaning of your word is:-",myDict.get(a))